from uuid import UUID
from datetime import datetime
from pydantic import BaseModel


class MessageCreate(BaseModel):

    receiver_id: UUID

    content: str


class MessageResponse(BaseModel):

    id: UUID

    sender_id: UUID

    receiver_id: UUID

    content: str

    created_at: datetime

    class Config:
        from_attributes = True