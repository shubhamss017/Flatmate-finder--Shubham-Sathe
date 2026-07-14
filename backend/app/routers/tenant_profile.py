from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db

from app.auth.dependencies import get_current_user

from app.schemas.tenant_profile import (
    TenantProfileCreate,
    TenantProfileResponse
)

from app.services.tenant_profile_service import (
    create_profile,
    get_profile,
    update_profile
)

router = APIRouter(
    prefix="/tenant/profile",
    tags=["Tenant Profile"]
)


@router.post(
    "",
    response_model=TenantProfileResponse
)
def create_tenant_profile(
    profile: TenantProfileCreate,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):

    if current_user["role"] != "tenant":
        raise HTTPException(
            status_code=403,
            detail="Only tenants can create profiles."
        )

    existing = get_profile(
        db,
        current_user["id"]
    )

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Profile already exists."
        )

    return create_profile(
        db,
        current_user["id"],
        profile
    )


@router.get(
    "/me",
    response_model=TenantProfileResponse
)
def my_profile(
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):

    profile = get_profile(
        db,
        current_user["id"]
    )

    if not profile:
        raise HTTPException(
            status_code=404,
            detail="Profile not found."
        )

    return profile


@router.put(
    "",
    response_model=TenantProfileResponse
)
def edit_profile(
    profile: TenantProfileCreate,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):

    db_profile = get_profile(
        db,
        current_user["id"]
    )

    if not db_profile:
        raise HTTPException(
            status_code=404,
            detail="Profile not found."
        )

    return update_profile(
        db,
        db_profile,
        profile
    )