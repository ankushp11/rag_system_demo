from app.utils.chunks_maker import chunk_text


def test_chunking_basic():
    text = "abcdefghijklmnopqrstuvwxyz" * 20
    chunks = chunk_text(text, chunk_size=100, overlap=20)
    assert len(chunks) > 0
    assert all(isinstance(chunk, str) for chunk in chunks)
