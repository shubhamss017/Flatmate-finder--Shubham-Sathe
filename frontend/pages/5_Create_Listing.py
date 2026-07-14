import streamlit as st
from datetime import date

from utils.session import init_session
from api.listing import create_listing, update_listing

# -------------------------
# PAGE CONFIG
# -------------------------
st.set_page_config(
    page_title="Create Listing",
    page_icon="🏠",
    layout="wide"
)

init_session()

if not st.session_state.logged_in:
    st.warning("Please login first.")
    st.stop()

if st.session_state.role != "owner":
    st.error("Only owners can create listings.")
    st.stop()

# -------------------------
# EDIT MODE
# -------------------------
editing = st.session_state.get("edit_listing")

st.title("🏠 Property Listing")

if editing:
    st.info("Editing Existing Listing")
else:
    st.info("Create New Listing")

# -------------------------
# FORM
# -------------------------
with st.form("listing_form"):

    col1, col2 = st.columns(2)

    with col1:

        title = st.text_input(
            "Title",
            value=editing["title"] if editing else ""
        )

        description = st.text_area(
            "Description",
            value=editing["description"] if editing else ""
        )

        location = st.text_input(
            "Location",
            value=editing["location"] if editing else ""
        )

        rent = st.number_input(
            "Monthly Rent",
            min_value=0,
            value=editing["rent"] if editing else 0
        )

        deposit = st.number_input(
            "Deposit",
            min_value=0,
            value=editing["deposit"] if editing else 0
        )

    with col2:

        property_type = st.selectbox(
            "Property Type",
            [
                "FLAT",
                "PG",
                "HOSTEL",
                "HOUSE"
            ],
            index=0
        )

        occupancy = st.number_input(
            "Occupancy",
            min_value=1,
            value=editing["occupancy"] if editing else 1
        )

        available_from = st.date_input(
            "Available From",
            value=date.today()
        )

        gender_preference = st.selectbox(
            "Gender Preference",
            [
                "ANY",
                "MALE",
                "FEMALE"
            ]
        )

        food_preference = st.selectbox(
            "Food Preference",
            [
                "ANY",
                "VEG",
                "NON_VEG"
            ]
        )

    st.markdown("### Amenities")

    c1, c2, c3 = st.columns(3)

    with c1:
        furnished = st.checkbox("Furnished")
        wifi = st.checkbox("WiFi")

    with c2:
        parking = st.checkbox("Parking")
        ac = st.checkbox("Air Conditioner")

    with c3:
        washing_machine = st.checkbox("Washing Machine")

    st.markdown("### House Rules")

    c1, c2, c3 = st.columns(3)

    with c1:
        smoking = st.checkbox("Smoking Allowed")

    with c2:
        drinking = st.checkbox("Drinking Allowed")

    with c3:
        pets = st.checkbox("Pets Allowed")

    submit = st.form_submit_button("💾 Save Listing")

# -------------------------
# SAVE
# -------------------------
if submit:

    payload = {

        "title": title,
        "description": description,
        "rent": rent,
        "deposit": deposit,
        "location": location,
        "property_type": property_type,
        "occupancy": occupancy,
        "available_from": str(available_from),

        "gender_preference": gender_preference,
        "food_preference": food_preference,

        "furnished": furnished,
        "wifi": wifi,
        "parking": parking,
        "ac": ac,
        "washing_machine": washing_machine,

        "smoking_allowed": smoking,
        "drinking_allowed": drinking,
        "pets_allowed": pets

    }

    if editing:

        response = update_listing(
            st.session_state.token,
            editing["id"],
            payload
        )

    else:

        response = create_listing(
            st.session_state.token,
            payload
        )

    if response.status_code in [200, 201]:

        st.success("Listing Saved Successfully ✅")

        if "edit_listing" in st.session_state:
            del st.session_state["edit_listing"]

        st.balloons()

    else:

        try:
            st.error(response.json())
        except:
            st.error("Something went wrong.")