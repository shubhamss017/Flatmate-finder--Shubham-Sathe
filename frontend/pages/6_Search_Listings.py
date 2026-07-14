import streamlit as st

from utils.session import init_session
from api.listing import search_listing
from api.interest import send_interest

st.set_page_config(
    page_title="Browse Listings",
    page_icon="🏠",
    layout="wide"
)

init_session()

if not st.session_state.logged_in:
    st.warning("Please Login")
    st.stop()

st.title("🔍 Browse Listings")

st.caption("Find your perfect flat using AI")

# =============================
# FILTERS
# =============================

c1, c2, c3, c4 = st.columns(4)

with c1:
    location = st.text_input(
        "Location",
        placeholder="Pune"
    )

with c2:
    min_rent = st.number_input(
        "Min Rent",
        value=0
    )

with c3:
    max_rent = st.number_input(
        "Max Rent",
        value=50000
    )

with c4:
    property_type = st.selectbox(
        "Property",
        [
            "",
            "FLAT",
            "PG",
            "HOUSE",
            "HOSTEL"
        ]
    )

if st.button("Search Listings", use_container_width=True):

    response = search_listing(
        st.session_state.token,
        location,
        min_rent,
        max_rent,
        property_type
    )

    if response.status_code == 200:

        listings = response.json()

        st.success(
            f"{len(listings)} Listings Found"
        )

        for listing in listings:

            with st.container(border=True):

                col1, col2 = st.columns([4,1])

                with col1:

                    st.subheader(
                        listing["title"]
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

                    st.write(
                        f"👥 Occupancy : {listing['occupancy']}"
                    )

                with col2:

                    if listing["wifi"]:
                        st.success("WiFi")

                    if listing["parking"]:
                        st.success("Parking")

                    if listing["ac"]:
                        st.success("AC")

                    if listing["furnished"]:
                        st.success("Furnished")

                st.divider()

                c1, c2 = st.columns(2)

                with c1:

                    if st.button(
                        "❤️ Interested",
                        key=f"interest_{listing['id']}"
                    ):

                        interest = send_interest(
                            st.session_state.token,
                            listing["id"]
                        )

                        if interest.status_code in [200,201]:

                            st.success(
                                "Interest Sent"
                            )

                        else:

                            st.error(
                                interest.json()
                            )

                with c2:

                    if st.button(
                        "View Details",
                        key=f"details_{listing['id']}"
                    ):

                        st.session_state.selected_listing = listing

                        st.switch_page(
                            "pages/7_AI_Matches.py"
                        )

    else:

        st.error(
            response.json()
        )