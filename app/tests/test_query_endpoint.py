from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_query_answer():
    payload = {
        "question": "What is this about?",
        "history": [["How does it work?", "It uses embeddings and LLM."]],
    }
    response = client.post("/query", json=payload)
    assert response.status_code == 200
