import os
os.environ["GOOGLE_API_KEY"] = ""
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_home():
    r = client.get("/")
    assert r.status_code == 200
    assert "FitBuddy" in r.text

def test_health():
    r = client.get("/api/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"

def test_ai_config_error():
    r = client.post("/api/generate-workout", json={
        "username":"Test User","user_id":"TEST-1","age":25,"weight":65,
        "goal":"general wellness","intensity":"medium"
    })
    assert r.status_code == 502
    assert "GOOGLE_API_KEY" in r.json()["detail"]
