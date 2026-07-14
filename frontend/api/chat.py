from api.client import (
    get,
    post
)


def get_conversations(token):

    return get(
        "/chat",
        token
    )


def get_messages(token, conversation_id):

    return get(
        f"/chat/{conversation_id}",
        token
    )


def send_message(
    token,
    conversation_id,
    message
):

    return post(
        "/chat/send",
        {
            "conversation_id": conversation_id,
            "message": message
        },
        token
    )