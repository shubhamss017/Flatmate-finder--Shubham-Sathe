import streamlit as st


def init_session():

    defaults = {

        "logged_in": False,

        "token": None,

        "user": None,

        "role": None

    }

    for key, value in defaults.items():

        if key not in st.session_state:

            st.session_state[key] = value


def login(token, user, role):

    st.session_state.logged_in = True

    st.session_state.token = token

    st.session_state.user = user

    st.session_state.role = role


def logout():

    for key in list(st.session_state.keys()):

        del st.session_state[key]
