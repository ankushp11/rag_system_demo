from sentence_transformers import SentenceTransformer


model = SentenceTransformer("intfloat/e5-small-v2")


def get_embedding(text: str) -> list:
    """
    Returns embedding for a given text using E5-small-v2 model.
    """
    formatted_text = f"passage: {text.strip()}"
    embedding = model.encode(formatted_text, convert_to_numpy=True)
    return embedding.tolist()  # ChromaDB accepts list[float]
