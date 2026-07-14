import streamlit as st

from utils.session import init_session
from api.listing import get_my_listings

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Owner Dashboard",
    page_icon="🏠",
    layout="wide"
)

init_session()

# -----------------------------
# Authentication Check
# -----------------------------
if not st.session_state.logged_in:
    st.warning("Please login first.")
    st.stop()

if st.session_state.role != "owner":
    st.error("Access Denied")
    st.stop()

# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:

    st.title("🏠 FlatMate AI")

    st.write(f"Welcome")

    st.success(st.session_state.user["email"])

    st.divider()

    st.page_link(
        "pages/5_Create_Listing.py",
        label="➕ Create Listing"
    )

    st.page_link(
        "pages/8_Interests.py",
        label="❤️ Interests"
    )

    st.page_link(
        "pages/9_Chat.py",
        label="💬 Chat"
    )

    st.page_link(
        "pages/10_Profile.py",
        label="👤 Profile"
    )

# -----------------------------
# Dashboard Title
# -----------------------------
st.title("🏠 Owner Dashboard")

st.write(
    "Manage your properties and view tenant activity."
)

# -----------------------------
# Load Listings
# -----------------------------
response = get_my_listings(
    st.session_state.token
)

if response.status_code == 200:

    listings = response.json()

else:

    listings = []

# -----------------------------
# Metrics
# -----------------------------
c1, c2, c3 = st.columns(3)

with c1:
    st.metric(
        "My Listings",
        len(listings)
    )

with c2:
    st.metric(
        "Interested Tenants",
        "0"
    )

with c3:
    st.metric(
        "Messages",
        "0"
    )

st.divider()

# -----------------------------
# Listings
# -----------------------------
st.subheader("📋 My Listings")

if len(listings) == 0:

    st.info(
        "No listings available."
    )

else:

    for listing in listings:

        with st.container():

            col1, col2 = st.columns([4,1])

            with col1:

                st.markdown(
                    f"### {listing['title']}"
                )

                st.write(
                    listing["description"]
                )

                st.write(
                    f"📍 {listing['location']}"
                )

                st.write(
                    f"💰 ₹ {listing['rent']}"
                )

                st.write(
                    f"🏠 {listing['property_type']}"
                )

            with col2:

                if st.button(
                    "✏ Edit",
                    key=f"edit_{listing['id']}"
                ):
                    st.session_state.edit_listing = listing

                    st.switch_page(
                        "pages/5_Create_Listing.py"
                    )

                if st.button(
                    "🗑 Delete",
                    key=f"delete_{listing['id']}"
                ):
                    st.warning(
                        "Delete API will be connected next."
                    )

            st.divider()