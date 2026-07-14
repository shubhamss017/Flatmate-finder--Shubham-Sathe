import streamlit as st

from utils.session import init_session
from api.profile import (
    get_profile,
    update_profile
)

st.set_page_config(
    page_title="Profile",
    page_icon="👤",
    layout="wide"
)

init_session()

if not st.session_state.logged_in:
    st.warning("Please Login")
    st.stop()

st.title("👤 My Profile")

response = get_profile(
    st.session_state.token
)

if response.status_code != 200:

    st.error("Unable to load profile")

    st.stop()

profile = response.json()

with st.form("profile"):

    st.subheader("Personal Information")

    full_name = st.text_input(
        "Full Name",
        value=profile.get("full_name","")
    )

    phone = st.text_input(
        "Phone",
        value=profile.get("phone","")
    )

    age = st.number_input(
        "Age",
        value=profile.get("age",18)
    )

    occupation = st.text_input(
        "Occupation",
        value=profile.get("occupation","")
    )

    bio = st.text_area(
        "Bio",
        value=profile.get("bio","")
    )

    if st.session_state.role == "tenant":

        st.subheader("Lifestyle")

        food = st.selectbox(
            "Food Preference",
            [
                "VEG",
                "NON_VEG",
                "ANY"
            ]
        )

        smoking = st.checkbox(
            "Smoking",
            value=profile.get(
                "smoking",
                False
            )
        )

        drinking = st.checkbox(
            "Drinking",
            value=profile.get(
                "drinking",
                False
            )
        )

        pets = st.checkbox(
            "Pets",
            value=profile.get(
                "pets",
                False
            )
        )

    save = st.form_submit_button(
        "💾 Save Profile"
    )

if save:

    payload = {

        "full_name":full_name,
        "phone":phone,
        "age":age,
        "occupation":occupation,
        "bio":bio

    }

    if st.session_state.role=="tenant":

        payload["food_preference"]=food
        payload["smoking"]=smoking
        payload["drinking"]=drinking
        payload["pets"]=pets

    response = update_profile(
        st.session_state.token,
        payload
    )

    if response.status_code==200:

        st.success("Profile Updated")

    else:

        st.error(response.json())