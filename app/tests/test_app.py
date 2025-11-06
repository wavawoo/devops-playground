from app import app

def test_root():
    client = app.test_client()
    resp = client.get("/")
    assert resp.status_code == 200
    data = resp.get_json()
    assert data["status"] == "ok"

def test_hello():
    client = app.test_client()
    resp = client.get("/hello?name=Ksusha")
    assert resp.status_code == 200
    data = resp.get_json()
    assert "Hello" in data["message"]
