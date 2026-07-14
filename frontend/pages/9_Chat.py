import streamlit as st

from utils.session import init_session
from api.chat import (
    get_conversations,
    get_messages,
    send_message
)

st.set_page_config(
    page_title="Chat",
    page_icon="💬",
    layout="wide"
)

init_session()

if not st.session_state.logged_in:
    st.warning("Please Login")
    st.stop()

st.title("💬 Messages")

# ----------------------------------
# Load Conversations
# ----------------------------------

response = get_conversations(
    st.session_state.token
)

if response.status_code == 200:
    conversations = response.json()
else:
    conversations = []

left, right = st.columns([1,2])

# =====================================
# LEFT PANEL
# =====================================

with left:

    st.subheader("Chats")

    if len(conversations) == 0:
        st.info("No Conversations")

    for chat in conversations:

        if st.button(
            f"💬 {chat['name']}",
            use_container_width=True,
            key=chat["conversation_id"]
        ):
            st.session_state.chat_id = chat["conversation_id"]
            st.rerun()

# =====================================
# RIGHT PANEL
# =====================================

with right:

    if "chat_id" not in st.session_state:

        st.info("Select a conversation")

    else:

        response = get_messages(
            st.session_state.token,
            st.session_state.chat_id
        )

        if response.status_code == 200:

            messages = response.json()

        else:

            messages = []

        st.subheader("Conversation")

        for message in messages:

            if message["is_me"]:

                st.chat_message("user").write(
                    message["message"]
                )

            else:

                st.chat_message("assistant").write(
                    message["message"]
                )

        new_message = st.chat_input(
            "Type message..."
        )

        if new_message:

            send = send_message(

                st.session_state.token,

                st.session_state.chat_id,

                new_message

            )

            if send.status_code in [200,201]:

                st.rerun()