from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import crud, schemas
from app.auth import get_current_user, admin_required
from app.database import get_db

router = APIRouter(prefix="/students", tags=["Students"])


@router.post("/", response_model=schemas.StudentResponse, status_code=status.HTTP_201_CREATED)
def add_student(
    student: schemas.StudentCreate,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user),
):
    existing_student = crud.get_student_by_email(db, student.email)

    if existing_student:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Student email already exists",
        )

    return crud.create_student(db, student)


@router.get("/", response_model=list[schemas.StudentResponse])
def list_students(
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user),
):
    return crud.get_students(db)


@router.get("/{student_id}", response_model=schemas.StudentResponse)
def get_student(
    student_id: int,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user),
):
    student = crud.get_student_by_id(db, student_id)

    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found",
        )

    return student


@router.put("/{student_id}", response_model=schemas.StudentResponse)
def update_student(
    student_id: int,
    student_data: schemas.StudentUpdate,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user),
):
    updated_student = crud.update_student(db, student_id, student_data)

    if not updated_student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found",
        )

    return updated_student


@router.delete("/{student_id}")
def delete_student(
    student_id: int,
    db: Session = Depends(get_db),
    current_user: dict = Depends(admin_required),
):
    deleted_student = crud.delete_student(db, student_id)

    if not deleted_student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found",
        )

    return {"message": "Student deleted successfully"}
