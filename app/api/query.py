from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Tuple
from app.utils.embedder import get_embedding
from app.utils.vectorstore import query_vectorstore
from app.utils.llm import generate_answer
from app.utils.memory import get_conversation_history, update_conversation_memory

router = APIRouter()


class QueryRequest(BaseModel):
    question: str
    history: List[Tuple[str, str]] = []


@router.post("/query")
async def query_document(req: QueryRequest):
    query = req.question

    query_embedding = get_embedding(query)
    top_chunks = query_vectorstore(query_embedding, top_k=3)

    docs = [chunk["text"] for chunk in top_chunks]
    sources = [chunk["metadata"] for chunk in top_chunks]

    history_list = req.history if req.history else get_conversation_history()
    history = [f"User: {q}\nAssistant: {a}" for q, a in history_list]

    answer = generate_answer(query, docs, chat_history=history)

    update_conversation_memory(query, answer)

    return {"answer": answer, "sources": sources}
