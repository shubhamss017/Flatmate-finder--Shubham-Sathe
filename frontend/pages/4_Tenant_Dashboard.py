import streamlit as st

from utils.session import init_session
from api.listing import get_all_listings
from api.matching import get_my_matches

# ---------------------------------
# PAGE CONFIG
# ---------------------------------

st.set_page_config(
    page_title="Tenant Dashboard",
    page_icon="🏠",
    layout="wide"
)

init_session()

# ---------------------------------
# AUTH CHECK
# ---------------------------------

if not st.session_state.logged_in:
    st.warning("Please Login")
    st.stop()

if st.session_state.role != "tenant":
    st.error("Access Denied")
    st.stop()

# ---------------------------------
# SIDEBAR
# ---------------------------------

with st.sidebar:

    st.title("🏠 FlatMate AI")

    st.success(st.session_state.user["email"])

    st.divider()

    st.page_link(
        "pages/6_Search_Listings.py",
        label="🔍 Browse Listings"
    )

    st.page_link(
        "pages/7_AI_Matches.py",
        label="🤖 AI Matches"
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

# ---------------------------------
# TITLE
# ---------------------------------

st.title("🏠 Tenant Dashboard")

st.caption("Find your perfect home using AI")

# ---------------------------------
# FETCH DATA
# ---------------------------------

listing_response = get_all_listings(
    st.session_state.token
)

match_response = get_my_matches(
    st.session_state.token
)

if listing_response.status_code == 200:
    listings = listing_response.json()
else:
    listings = []

if match_response.status_code == 200:
    matches = match_response.json()
else:
    matches = []

# ---------------------------------
# METRICS
# ---------------------------------

c1, c2, c3 = st.columns(3)

with c1:
    st.metric(
        "Available Listings",
        len(listings)
    )

with c2:
    st.metric(
        "AI Matches",
        len(matches)
    )

with c3:
    st.metric(
        "Saved Interests",
        "0"
    )

st.divider()

# ---------------------------------
# TOP AI MATCHES
# ---------------------------------

st.subheader("🤖 Top AI Matches")

if len(matches) == 0:

    st.info("No AI Matches Yet")

else:

    for match in matches[:5]:

        with st.container():

            st.markdown(
                f"### 🏠 {match['listing_title']}"
            )

            st.write(
                f"📍 {match['location']}"
            )

            st.write(
                f"💰 ₹ {match['rent']}"
            )

            st.progress(
                match["match_score"]/100
            )

            st.success(
                f"Compatibility : {match['match_score']}%"
            )

            st.write(
                match["reason"]
            )

            if st.button(
                "View Listing",
                key=match["listing_id"]
            ):
                st.info(
                    "Detailed page coming next."
                )

            st.divider()

# ---------------------------------
# RECENT LISTINGS
# ---------------------------------

st.subheader("🆕 Latest Listings")

for listing in listings[:5]:

    with st.expander(listing["title"]):

        st.write(listing["description"])

        st.write(
            f"📍 {listing['location']}"
        )

        st.write(
            f"💰 ₹ {listing['rent']}"
        )

        st.write(
            f"🏠 {listing['property_type']}"
        )

        if st.button(
            "❤️ Interested",
            key=f"interest_{listing['id']}"
        ):
            st.success(
                "Interest API will be connected next."
            )