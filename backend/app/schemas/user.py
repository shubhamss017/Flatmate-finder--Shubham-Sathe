from pydantic import BaseModel, EmailStr, Field


class UserRegister(BaseModel):
    email: EmailStr
    password: str = Field(
        min_length=8,
        max_length=100
    )
    role: str


class UserResponse(BaseModel):
    id: str
    email: EmailStr
    role: str