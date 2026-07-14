import streamlit as st

from utils.session import init_session
from api.interest import (
    received_interest,
    sent_interest,
    accept_interest,
    reject_interest
)

st.set_page_config(
    page_title="Interests",
    page_icon="❤️",
    layout="wide"
)

init_session()

if not st.session_state.logged_in:
    st.warning("Please login first.")
    st.stop()

st.title("❤️ Interests")

# ===================================================
# OWNER
# ===================================================

if st.session_state.role == "owner":

    response = received_interest(
        st.session_state.token
    )

    if response.status_code == 200:

        interests = response.json()

    else:

        interests = []

    st.subheader("Received Requests")

    if len(interests) == 0:

        st.info("No Requests Yet")

    for interest in interests:

        with st.container(border=True):

            st.subheader(
                interest["tenant_name"]
            )

            st.write(
                f"Listing : {interest['listing_title']}"
            )

            st.write(
                f"Budget : ₹ {interest['budget']}"
            )

            st.write(
                f"Occupation : {interest['occupation']}"
            )

            st.write(
                interest["bio"]
            )

            c1, c2 = st.columns(2)

            with c1:

                if st.button(
                    "✅ Accept",
                    key=f"a_{interest['interest_id']}"
                ):

                    r = accept_interest(
                        st.session_state.token,
                        interest["interest_id"]
                    )

                    if r.status_code == 200:

                        st.success(
                            "Interest Accepted"
                        )

                        st.rerun()

            with c2:

                if st.button(
                    "❌ Reject",
                    key=f"r_{interest['interest_id']}"
                ):

                    r = reject_interest(
                        st.session_state.token,
                        interest["interest_id"]
                    )

                    if r.status_code == 200:

                        st.success(
                            "Interest Rejected"
                        )

                        st.rerun()

            st.divider()

# ===================================================
# TENANT
# ===================================================

else:

    response = sent_interest(
        st.session_state.token
    )

    if response.status_code == 200:

        interests = response.json()

    else:

        interests = []

    st.subheader("Sent Requests")

    if len(interests) == 0:

        st.info("No Interests Sent")

    for interest in interests:

        with st.container(border=True):

            st.subheader(
                interest["listing_title"]
            )

            st.write(
                f"Owner : {interest['owner_name']}"
            )

            st.write(
                f"Status : {interest['status']}"
            )

            if interest["status"] == "accepted":

                st.success(
                    "Accepted ✅"
                )

                st.button(
                    "💬 Open Chat",
                    key=f"chat_{interest['interest_id']}"
                )

            elif interest["status"] == "pending":

                st.warning("Pending")

            else:

                st.error("Rejected")

            st.divider()