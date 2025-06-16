from app.utils.vectorstore import add_to_vectorstore, query_vectorstore
from app.utils.embedder import get_embedding


def test_add_and_query_vectorstore():
    text = "Sample vector test text"
    emb = get_embedding(text)
    add_to_vectorstore([text], [emb], [{"source": "test.txt", "page": 1}])

    results = query_vectorstore(emb, top_k=1)
    assert isinstance(results, list)
    assert len(results) > 0
    assert "text" in results[0]
