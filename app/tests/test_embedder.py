from app.utils.embedder import get_embedding


def test_get_embedding_shape():
    text = "This is a test sentence."
    embedding = get_embedding(text)
    assert isinstance(embedding, list)
    assert all(isinstance(x, float) for x in embedding)
