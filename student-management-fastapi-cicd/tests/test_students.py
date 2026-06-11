from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def get_token():
    client.post(
        "/auth/register",
        json={
            "username": "studentadmin",
            "email": "studentadmin@example.com",
            "password": "admin123",
            "role": "admin",
        },
    )

    response = client.post(
        "/auth/login",
        data={"username": "studentadmin", "password": "admin123"},
    )

    return response.json()["access_token"]


def test_create_student():
    token = get_token()

    response = client.post(
        "/students/",
        json={
            "name": "Krishna",
            "email": "krishna_test@example.com",
            "course": "Python FastAPI",
            "phone": "9999999999",
        },
        headers={"Authorization": f"Bearer {token}"},
    )

    assert response.status_code in [201, 400]


def test_get_students():
    token = get_token()

    response = client.get(
        "/students/",
        headers={"Authorization": f"Bearer {token}"},
    )

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_students_without_token():
    response = client.get("/students/")

    assert response.status_code == 401
