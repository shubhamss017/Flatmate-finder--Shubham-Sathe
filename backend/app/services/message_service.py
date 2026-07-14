from sqlalchemy.orm import Session
from sqlalchemy import or_, and_

from app.models.message import Message


def send_message(
    db: Session,
    sender_id,
    receiver_id,
    content
):

    message = Message(
        sender_id=sender_id,
        receiver_id=receiver_id,
        content=content
    )

    db.add(message)
    db.commit()
    db.refresh(message)

    return message


def get_conversation(
    db: Session,
    user1,
    user2
):

    return (
        db.query(Message)
        .filter(
            or_(
                and_(
                    Message.sender_id == user1,
                    Message.receiver_id == user2
                ),
                and_(
                    Message.sender_id == user2,
                    Message.receiver_id == user1
                )
            )
        )
        .order_by(Message.created_at.asc())
        .all()
    )