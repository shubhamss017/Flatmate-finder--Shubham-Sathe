import streamlit as st

from api.auth import login

from utils.session import login as save_login

st.title("🔐 Login")

email = st.text_input("Email")

password = st.text_input(

    "Password",

    type="password"

)

if st.button("Login"):

    response = login({

        "email": email,

        "password": password

    })

    if response.status_code == 200:

        data = response.json()

        token = data["access_token"]

        # NOTE: Replace these with your actual backend response or decode JWT if needed
        user = {"email": email}
        role = data.get("role", "tenant")

        save_login(token, user, role)

        st.success("Login Successful")

        st.rerun()

    else:

        st.error(response.json()["detail"])