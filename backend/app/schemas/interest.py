from uuid import UUID

from pydantic import BaseModel

from app.models.enums import InterestStatus


class InterestCreate(BaseModel):

    listing_id: UUID


class InterestResponse(BaseModel):

    id: UUID

    tenant_id: UUID

    listing_id: UUID

    status: InterestStatus

    class Config:
        from_attributes = True