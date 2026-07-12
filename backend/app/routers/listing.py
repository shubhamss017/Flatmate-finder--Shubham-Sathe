from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db

from app.schemas.listing import (
    ListingCreate,
    ListingResponse
)

from app.services.listing_service import (
    create_listing,
    get_all_listings,
    get_listing_by_id
)

from app.auth.dependencies import get_current_user

router = APIRouter(
    prefix="/listings",
    tags=["Listings"]
)


@router.post(
    "",
    response_model=ListingResponse
)
def create_new_listing(
    listing: ListingCreate,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):

    if current_user["role"] != "owner":
        raise HTTPException(
            status_code=403,
            detail="Only owners can create listings."
        )

    return create_listing(
        db,
        current_user["id"],
        listing
    )


@router.get(
    "",
    response_model=list[ListingResponse]
)
def get_listings(
    db: Session = Depends(get_db)
):
    return get_all_listings(db)


@router.get(
    "/{listing_id}",
    response_model=ListingResponse
)
def get_listing(
    listing_id,
    db: Session = Depends(get_db)
):

    listing = get_listing_by_id(
        db,
        listing_id
    )

    if not listing:
        raise HTTPException(
            status_code=404,
            detail="Listing not found"
        )

    return listing