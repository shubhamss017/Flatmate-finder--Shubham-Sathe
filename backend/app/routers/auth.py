from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.schemas.user import UserLogin
from app.auth.hashing import verify_password
from app.auth.jwt_handler import create_access_token

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
    db=db,
    email=user.email,
    password=hashed_password,
    role=user.role
    )

    return {
        "message": "User registered successfully",
        "email": created_user.email,
        "role": created_user.role
    }
@router.post("/login")
def login(
    user: UserLogin,
    db: Session = Depends(get_db)
):
    db_user = get_user_by_email(db, user.email)

    if not db_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    if not verify_password(
        user.password,
        db_user.password
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    token = create_access_token(
        {
            "sub": str(db_user.id),
            "email": db_user.email,
            "role": db_user.role
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }