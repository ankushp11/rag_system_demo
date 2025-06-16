from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_upload_txt_file():
    files = {"file": ("test.txt", b"Hello world from test!", "text/plain")}
    response = client.post("/upload", files=files)
    assert response.status_code == 200
    assert "chunks_added" in response.json()
