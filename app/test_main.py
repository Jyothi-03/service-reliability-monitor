from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_home():
    res = client.get("/")
    assert res.status_code == 200

def test_add_service():
    res = client.post("/services", json={"url": "https://example.com"})
    assert res.status_code == 200
    assert "id" in res.json()

def test_list_services():
    res = client.get("/services")
    assert res.status_code == 200

def test_status():
    res = client.get("/status")
    assert res.status_code == 200