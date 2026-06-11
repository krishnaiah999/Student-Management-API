from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_register_user():
    response = client.post(
        "/auth/register",
        json={
            "username": "admin",
            "email": "admin@example.com",
            "password": "admin123",
            "role": "admin",
        },
    )

    assert response.status_code in [201, 400]


def test_login_success():
    client.post(
        "/auth/register",
        json={
            "username": "loginadmin",
            "email": "loginadmin@example.com",
            "password": "admin123",
            "role": "admin",
        },
    )

    response = client.post(
        "/auth/login",
        data={"username": "loginadmin", "password": "admin123"},
    )

    assert response.status_code == 200
    assert "access_token" in response.json()


def test_login_failure():
    response = client.post(
        "/auth/login",
        data={"username": "wrong", "password": "wrong"},
    )

    assert response.status_code == 401