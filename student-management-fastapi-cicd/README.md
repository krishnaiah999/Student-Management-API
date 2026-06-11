# Student Management FastAPI CI/CD Project

This is an interview-ready FastAPI project with:

- FastAPI CRUD APIs
- SQLAlchemy ORM
- SQLite database for easy local practice
- Pydantic validation
- JWT authentication
- Pytest test cases
- Dockerfile
- Docker Compose
- GitHub Actions CI pipeline

## Run locally

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open Swagger:

```text
http://127.0.0.1:8000/docs
```

## Default login user

```text
username: admin
password: admin123
```

## Run tests

```bash
pytest
```

## Run with Docker

```bash
docker build -t student-fastapi .
docker run -d -p 8000:8000 student-fastapi
```

## Run with Docker Compose

```bash
docker compose up --build
```

## CI/CD Flow

Whenever code is pushed to GitHub main branch:

1. GitHub Actions checks out code
2. Sets up Python
3. Installs dependencies
4. Runs pytest
5. Builds Docker image

This proves CI pipeline. Later you can add EC2 deployment.
