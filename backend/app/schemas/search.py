from typing import Optional
from pydantic import BaseModel
from uuid import UUID
from datetime import date

from app.models.enums import (
    PropertyType,
    FoodPreference,
    GenderPreference
)


class SearchResponse(BaseModel):

    id: UUID

    owner_id: UUID

    title: str

    description: str

    rent: int

    deposit: int

    location: str

    property_type: PropertyType

    occupancy: int

    available_from: date

    furnished: bool

    parking: bool

    wifi: bool

    ac: bool

    washing_machine: bool

    gender_preference: GenderPreference

    food_preference: FoodPreference

    smoking_allowed: bool

    drinking_allowed: bool

    pets_allowed: bool

    class Config:
        from_attributes = True