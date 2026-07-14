import streamlit as st


def load_css():

    st.markdown("""

<style>

.stApp{

background:#F8FAFC;

}

.big-title{

font-size:40px;

font-weight:bold;

color:#4F46E5;

text-align:center;

margin-bottom:10px;

}

.subtitle{

text-align:center;

color:#64748B;

font-size:18px;

margin-bottom:30px;

}

.block{

background:white;

padding:25px;

border-radius:15px;

box-shadow:0px 5px 15px rgba(0,0,0,.08);

}

div.stButton>button{

background:#4F46E5;

color:white;

border-radius:10px;

height:45px;

width:100%;

font-size:17px;

}

</style>

""", unsafe_allow_html=True)