# from fastapi import APIRouter, HTTPException, status
# from fastapi.security import OAuth2PasswordRequestForm
# from fastapi import Depends

# from app.auth import authenticate_user, create_access_token
# from app.schemas import Token

# router = APIRouter(prefix="/auth", tags=["Authentication"])


# @router.post("/login", response_model=Token)
# def login(form_data: OAuth2PasswordRequestForm = Depends()):
#     is_valid_user = authenticate_user(form_data.username, form_data.password)

#     if not is_valid_user:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Invalid username or password",
#         )

#     token = create_access_token(data={"sub": form_data.username})

#     return {
#         "access_token": token,
#         "token_type": "bearer",
#     }

#extension1
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app import crud, schemas
from app.auth import authenticate_user, create_access_token, hash_password
from app.database import get_db

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/register", response_model=schemas.UserResponse, status_code=status.HTTP_201_CREATED)
def register_user(
    user: schemas.UserCreate,
    db: Session = Depends(get_db),
):
    existing_username = crud.get_user_by_username(db, user.username)

    if existing_username:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already exists",
        )

    existing_email = crud.get_user_by_email(db, user.email)

    if existing_email:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already exists",
        )

    hashed_password = hash_password(user.password)

    return crud.create_user(db, user, hashed_password)


@router.post("/login", response_model=schemas.Token)
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    is_valid_user = authenticate_user(form_data.username, form_data.password)

    if not is_valid_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
        )

    token = create_access_token(data={"sub": form_data.username})

    return {
        "access_token": token,
        "token_type": "bearer",
    }