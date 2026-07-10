from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID
import uuid

from app.database.base import BaseModel


class OwnerProfile(BaseModel):
    __tablename__ = "owner_profiles"

    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
        unique=True
    )

    full_name: Mapped[str] = mapped_column(
        String(100)
    )

    phone: Mapped[str] = mapped_column(
        String(20)
    )

    property_name: Mapped[str] = mapped_column(
        String(150)
    )

    property_address: Mapped[str] = mapped_column(
        String(250)
    )

    user = relationship(
        "User",
        back_populates="owner_profile"
    )