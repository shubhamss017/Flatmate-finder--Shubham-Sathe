from fastapi import APIRouter
from fastapi import WebSocket
from fastapi import WebSocketDisconnect
from app.database.connection import SessionLocal
from app.services.message_service import send_message

from app.websocket.connection_manager import manager

router = APIRouter()


@router.websocket("/ws/{user_id}")

async def websocket_chat(
    websocket: WebSocket,
    user_id: str
):

    await manager.connect(
        user_id,
        websocket
    )

    try:

        while True:

            data = await websocket.receive_json()

            await manager.send_personal_message(

                data["receiver_id"],

                {

                    "sender_id": user_id,

                    "content": data["content"]

                }

            )
            db = SessionLocal()

            send_message(

            db,

            user_id,

            data["receiver_id"],

            data["content"]

            )

            db.close()
            

    except WebSocketDisconnect:

        manager.disconnect(
            user_id
        )