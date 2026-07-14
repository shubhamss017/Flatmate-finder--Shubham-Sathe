import uuid

from sqlalchemy import Enum
from sqlalchemy import ForeignKey

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from sqlalchemy.dialects.postgresql import UUID

from app.database.base import BaseModel

from app.models.enums import InterestStatus


class Interest(BaseModel):

    __tablename__ = "interests"

    tenant_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id")
    )

    listing_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("listings.id")
    )

    status: Mapped[InterestStatus] = mapped_column(
        Enum(InterestStatus),
        default=InterestStatus.PENDING
    )

    tenant = relationship("User")

    listing = relationship("Listing")