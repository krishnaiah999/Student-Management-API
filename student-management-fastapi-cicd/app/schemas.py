from pydantic import BaseModel, EmailStr, Field


class StudentCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    email: EmailStr
    course: str = Field(..., min_length=2, max_length=100)
    phone: str | None = Field(default=None, max_length=20)


class StudentUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=2, max_length=100)
    email: EmailStr | None = None
    course: str | None = Field(default=None, min_length=2, max_length=100)
    phone: str | None = Field(default=None, max_length=20)


class StudentResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    course: str
    phone: str | None = None

    model_config = {
        "from_attributes": True
    }


class Token(BaseModel):
    access_token: str
    token_type: str
class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(..., min_length=6, max_length=100)
    role: str = "user"


class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    role: str

    model_config = {
        "from_attributes": True
    }


class LoginResponse(BaseModel):
    access_token: str
    token_type: str