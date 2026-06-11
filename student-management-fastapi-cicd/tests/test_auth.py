from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_login_success():
    response = client.post(
        "/auth/login",
        data={"username": "admin", "password": "admin123"},
    )

    assert response.status_code == 200
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"


def test_login_failure():
    response = client.post(
        "/auth/login",
        data={"username": "wrong", "password": "wrong"},
    )

    assert response.status_code == 401
