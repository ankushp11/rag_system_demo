import os
from fastapi import APIRouter, UploadFile, File, HTTPException
from app.utils.file_parser import parse_file
from app.utils.chunks_maker import chunk_text
from app.utils.embedder import get_embedding
from app.utils.vectorstore import add_to_vectorstore

router = APIRouter()


@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    filename = file.filename
    extension = filename.split(".")[-1].lower()

    if extension not in ["txt", "pdf"]:
        raise HTTPException(
            status_code=400, detail="Only .txt or .pdf files are supported."
        )

    os.makedirs("tmp", exist_ok=True)
    temp_path = os.path.join("tmp", filename)

    with open(temp_path, "wb") as f:
        content = await file.read()
        f.write(content)

    parsed_output = parse_file(filename, content)
    os.remove(temp_path)

    chunks = []
    metadatas = []

    for page_num, text in parsed_output:
        text_chunks = chunk_text(text)
        chunks.extend(text_chunks)
        metadatas.extend([{"source": filename, "page": page_num} for _ in text_chunks])

    embeddings = [get_embedding(chunk) for chunk in chunks]
    add_to_vectorstore(chunks, embeddings, metadatas)

    return {
        "message": f"File '{filename}' uploaded and processed successfully.",
        "chunks_added": len(chunks),
    }
