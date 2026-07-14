from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.auth.dependencies import get_current_user

from app.schemas.message import (
    MessageCreate,
    MessageResponse
)

from app.services.message_service import (
    send_message,
    get_conversation
)

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)


@router.post(
    "",
    response_model=MessageResponse
)
def send(
    message: MessageCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return send_message(
        db,
        current_user["id"],
        message.receiver_id,
        message.content
    )


@router.get(
    "/{user_id}",
    response_model=list[MessageResponse]
)
def conversation(
    user_id: UUID,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return get_conversation(
        db,
        current_user["id"],
        user_id
    )