import streamlit as st

from api.auth import register

st.title("📝 Register")

email = st.text_input("Email")

password = st.text_input(

    "Password",

    type="password"

)

role = st.selectbox(

    "Role",

    ["tenant", "owner"]

)

if st.button("Register"):

    response = register({

        "email": email,

        "password": password,

        "role": role

    })

    if response.status_code == 200:

        st.success("Registration Successful")

    else:

        st.error(response.json()["detail"])