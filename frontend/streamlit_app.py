import streamlit as st

from utils.session import init_session
from utils.styles import load_css

st.set_page_config(

    page_title="FlatMate AI",

    page_icon="🏠",

    layout="wide"

)

init_session()

load_css()

st.markdown(

    "<div class='big-title'>🏠 FlatMate AI</div>",

    unsafe_allow_html=True

)

st.markdown(

    "<div class='subtitle'>Find Your Perfect Flatmate Using Artificial Intelligence</div>",

    unsafe_allow_html=True

)

col1, col2 = st.columns(2)

with col1:

    st.image(

        "https://images.unsplash.com/photo-1522708323590-d24dbb6b0267",

        use_container_width=True

    )

with col2:

    st.markdown("""

### Features

✅ AI Flatmate Matching

✅ Lifestyle Compatibility

✅ Owner & Tenant Dashboard

✅ Real Time Chat

✅ Secure Authentication

✅ Smart Recommendations

---

Use the navigation on the left to Login or Register.

""")