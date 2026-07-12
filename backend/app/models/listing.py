import uuid
from datetime import date

from sqlalchemy import (
    String,
    Integer,
    Boolean,
    ForeignKey,
    Date,
    Text,
    Enum
)

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import BaseModel
from app.models.enums import (
    PropertyType,
    FoodPreference,
    GenderPreference
)


class Listing(BaseModel):
    __tablename__ = "listings"

    owner_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
        nullable=False
    )

    title: Mapped[str] = mapped_column(
        String(150),
        nullable=False
    )

    description: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    rent: Mapped[int] = mapped_column(Integer)

    deposit: Mapped[int] = mapped_column(Integer)

    location: Mapped[str] = mapped_column(
        String(150)
    )

    property_type: Mapped[PropertyType] = mapped_column(Enum(PropertyType))


    occupancy: Mapped[int] = mapped_column(Integer)

    available_from: Mapped[date] = mapped_column(Date)

    furnished: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )

    parking: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )

    wifi: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )

    ac: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )

    washing_machine: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )

    gender_preference: Mapped[GenderPreference] = mapped_column(
    Enum (GenderPreference)
    )

    food_preference: Mapped[FoodPreference] = mapped_column(
    Enum (FoodPreference)
    )


    smoking_allowed: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )

    drinking_allowed: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )

    pets_allowed: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )

    owner = relationship(
    "User",
    back_populates="listings"
)