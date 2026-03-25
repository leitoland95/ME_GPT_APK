import pytest
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_index_served():
    resp = client.get("/")
    assert resp.status_code == 200
    assert "<title>My PWA Project</title>" in resp.text

def test_manifest_and_sw():
    m = client.get("/static/manifest.json")
    s = client.get("/static/sw.js")
    assert m.status_code == 200
    assert s.status_code == 200