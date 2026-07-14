from typing import Optional

from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.session import get_db

from app.models.enums import (
    PropertyType,
    FoodPreference
)

from app.schemas.search import SearchResponse

from app.services.search_service import search_listings

router = APIRouter(
    prefix="/search",
    tags=["Search"]
)


@router.get(
    "/listings",
    response_model=list[SearchResponse]
)
def search(

    location: Optional[str] = None,

    min_rent: Optional[int] = None,

    max_rent: Optional[int] = None,

    property_type: Optional[PropertyType] = None,

    food_preference: Optional[FoodPreference] = None,

    wifi: Optional[bool] = None,

    parking: Optional[bool] = None,

    ac: Optional[bool] = None,

    db: Session = Depends(get_db)

):

    return search_listings(

        db,

        location,

        min_rent,

        max_rent,

        property_type,

        food_preference,

        wifi,

        parking,

        ac

    )