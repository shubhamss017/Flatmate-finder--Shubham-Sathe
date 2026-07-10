from pydantic import BaseModel, EmailStr, Field

from app.models.enums import UserRole


class UserRegister(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)
    role: UserRole


class UserLogin(BaseModel):
    email: EmailStr
    password: str