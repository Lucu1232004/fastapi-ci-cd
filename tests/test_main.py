from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello CI/CD"}


def test_greet():
    response = client.get("/greet?name=Alex")  # <--- Con query param
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, Alex!"}
