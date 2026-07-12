from datetime import date
from uuid import UUID

from pydantic import BaseModel

from app.models.enums import (
    PropertyType,
    FoodPreference,
    GenderPreference
)


class ListingCreate(BaseModel):
    title: str
    description: str
    rent: int
    deposit: int
    location: str

    property_type: PropertyType

    occupancy: int

    available_from: date

    furnished: bool = False
    parking: bool = False
    wifi: bool = False
    ac: bool = False
    washing_machine: bool = False

    gender_preference: GenderPreference

    food_preference: FoodPreference

    smoking_allowed: bool = False
    drinking_allowed: bool = False
    pets_allowed: bool = False


class ListingResponse(ListingCreate):
    id: UUID
    owner_id: UUID

    class Config:
        from_attributes = True