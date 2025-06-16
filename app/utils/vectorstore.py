from chromadb import PersistentClient
from .helper import get_doc_hash

client = PersistentClient(path="./chroma_db")


collection = client.get_or_create_collection(name="rag_docs")


def add_to_vectorstore(
    texts: list[str], embeddings: list[list[float]], metadatas: list[dict]
):
    for i, (text, emb, meta) in enumerate(zip(texts, embeddings, metadatas)):
        doc_hash = get_doc_hash(text)
        try:
            collection.add(
                documents=[text], embeddings=[emb], metadatas=[meta], ids=[doc_hash]
            )
        except Exception as e:
            if "already exists" in str(e):
                print(f"Skipped duplicate chunk: {doc_hash}")
            else:
                raise e


def query_vectorstore(query_embedding: list[float], top_k=3):
    """
    Query ChromaDB for most relevant documents given a query embedding.
    Returns: list of dicts with document + metadata
    """
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k,
        include=["documents", "metadatas"],
    )
    docs = results["documents"][0]
    metas = results["metadatas"][0]
    return [{"text": d, "metadata": m} for d, m in zip(docs, metas)]
