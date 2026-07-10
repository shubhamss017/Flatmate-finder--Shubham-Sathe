from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID
import uuid

from app.database.base import BaseModel


class TenantProfile(BaseModel):
    __tablename__ = "tenant_profiles"

    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
        unique=True
    )

    full_name: Mapped[str] = mapped_column(String(100))

    age: Mapped[int] = mapped_column(Integer)

    occupation: Mapped[str] = mapped_column(String(100))

    budget: Mapped[int] = mapped_column(Integer)

    preferred_location: Mapped[str] = mapped_column(
        String(150)
    )

    bio: Mapped[str] = mapped_column(String(500))

    user = relationship(
        "User",
        back_populates="tenant_profile"
    )