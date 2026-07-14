import uuid

from sqlalchemy import (
    String,
    Integer,
    Boolean,
    ForeignKey,
    Enum
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import BaseModel
from app.models.enums import FoodPreference


class TenantProfile(BaseModel):
    __tablename__ = "tenant_profiles"

    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
        unique=True
    )

    full_name: Mapped[str] = mapped_column(
        String(100)
    )

    age: Mapped[int] = mapped_column(
        Integer
    )

    occupation: Mapped[str] = mapped_column(
        String(100)
    )

    budget: Mapped[int] = mapped_column(
        Integer
    )

    preferred_location: Mapped[str] = mapped_column(
        String(150)
    )

    bio: Mapped[str] = mapped_column(
        String(500)
    )

    food_preference: Mapped[FoodPreference] = mapped_column(
        Enum(FoodPreference)
    )

    smoking: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )

    drinking: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )

    pets: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )

    cleanliness: Mapped[int] = mapped_column(
        Integer
    )

    sleep_schedule: Mapped[str] = mapped_column(
        String(20)
    )

    work_mode: Mapped[str] = mapped_column(
        String(30)
    )

    languages: Mapped[str] = mapped_column(
        String(200)
    )

    hobbies: Mapped[str] = mapped_column(
        String(500)
    )

    user = relationship(
        "User",
        back_populates="tenant_profile"
    )