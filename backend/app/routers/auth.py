from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.user import UserRegister
from app.services.user_service import (
    create_user,
    get_user_by_email
)
from app.auth.hashing import hash_password

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/register")
def register(
    user: UserRegister,
    db: Session = Depends(get_db)
):

    existing_user = get_user_by_email(
        db,
        user.email
    )

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    hashed_password = hash_password(
        user.password
    )

    created_user = create_user(
        db,
        user.email,
        hashed_password,
        user.role
    )

    return {
        "message": "User registered successfully",
        "email": created_user.email,
        "role": created_user.role
    }