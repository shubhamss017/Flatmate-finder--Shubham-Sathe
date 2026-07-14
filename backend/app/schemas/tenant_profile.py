from pydantic import BaseModel
from uuid import UUID

from app.models.enums import FoodPreference


class TenantProfileCreate(BaseModel):
    full_name: str
    age: int
    occupation: str
    budget: int
    preferred_location: str
    bio: str

    food_preference: FoodPreference

    smoking: bool
    drinking: bool
    pets: bool

    cleanliness: int

    sleep_schedule: str

    work_mode: str

    languages: str

    hobbies: str


class TenantProfileResponse(TenantProfileCreate):
    id: UUID
    user_id: UUID

    class Config:
        from_attributes = True