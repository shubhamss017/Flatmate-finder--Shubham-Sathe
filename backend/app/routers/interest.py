from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.auth.dependencies import get_current_user

from app.schemas.interest import (
    InterestCreate,
    InterestResponse
)

from app.models.enums import InterestStatus

from app.services.interest_service import *

router = APIRouter(
    prefix="/interest",
    tags=["Interest"]
)


@router.post(
    "",
    response_model=InterestResponse
)
def send_interest(
    data: InterestCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    interest = create_interest(
        db,
        current_user["id"],
        data.listing_id
    )

    if not interest:
        raise HTTPException(
            status_code=400,
            detail="Already interested"
        )

    return interest


@router.get(
    "/my",
    response_model=list[InterestResponse]
)
def my_interests(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return get_my_interests(
        db,
        current_user["id"]
    )


@router.patch(
    "/{interest_id}",
    response_model=InterestResponse
)
def update_status(
    interest_id: UUID,
    status: InterestStatus,
    db: Session = Depends(get_db)
):

    interest = update_interest_status(
        db,
        interest_id,
        status
    )

    if not interest:
        raise HTTPException(
            status_code=404,
            detail="Interest not found"
        )

    return interest


@router.delete("/{interest_id}")
def remove_interest(
    interest_id: UUID,
    db: Session = Depends(get_db)
):

    success = delete_interest(
        db,
        interest_id
    )

    if not success:
        raise HTTPException(
            status_code=404,
            detail="Interest not found"
        )

    return {
        "message": "Interest removed"
    }