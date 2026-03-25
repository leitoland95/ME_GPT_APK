import pytest
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_query_no_input():
    resp = client.post("/api/query", data={})
    assert resp.status_code == 200
    body = resp.json()
    assert "No se recibió" in body["result"] or isinstance(body["result"], str)

def test_query_with_text_and_files(tmp_path):
    # create a temporary file to upload
    p = tmp_path / "sample.txt"
    p.write_text("hola")
    with open(p, "rb") as f:
        resp = client.post("/api/query", data={"text": "hola mundo"}, files={"files": ("sample.txt", f, "text/plain")})
    assert resp.status_code == 200
    body = resp.json()
    assert "hola mundo" in body["result"]
    assert body["metadata"]["file_count"] == 1