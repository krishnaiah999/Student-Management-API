from fastapi import FastAPI

from app.database import Base, engine
from app.routers import auth, students

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Student Management API",
    description="FastAPI project with CRUD, JWT, Docker and CI/CD pipeline",
    version="1.0.0",
)

@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok"}


app.include_router(auth.router)
app.include_router(students.router)
