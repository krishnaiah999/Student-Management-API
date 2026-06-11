from sqlalchemy.orm import Session

from app import models, schemas


def create_student(db: Session, student: schemas.StudentCreate):
    new_student = models.Student(**student.model_dump())
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student


def get_students(db: Session):
    return db.query(models.Student).all()


def get_student_by_id(db: Session, student_id: int):
    return db.query(models.Student).filter(models.Student.id == student_id).first()


def get_student_by_email(db: Session, email: str):
    return db.query(models.Student).filter(models.Student.email == email).first()


def update_student(db: Session, student_id: int, student_data: schemas.StudentUpdate):
    student = get_student_by_id(db, student_id)

    if not student:
        return None

    update_data = student_data.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(student, key, value)

    db.commit()
    db.refresh(student)
    return student


def delete_student(db: Session, student_id: int):
    student = get_student_by_id(db, student_id)

    if not student:
        return None

    db.delete(student)
    db.commit()
    return student
def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def create_user(db: Session, user: schemas.UserCreate, hashed_password: str):
    new_user = models.User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password,
        role=user.role,
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user