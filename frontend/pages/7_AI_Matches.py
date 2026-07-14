import streamlit as st

from utils.session import init_session
from api.matching import get_my_matches
from api.interest import send_interest

st.set_page_config(
    page_title="AI Matches",
    page_icon="🤖",
    layout="wide"
)

init_session()

if not st.session_state.logged_in:
    st.warning("Please login first.")
    st.stop()

st.title("🤖 AI Flatmate Matching")

st.caption(
    "Our AI recommends the best properties based on your lifestyle and preferences."
)

response = get_my_matches(
    st.session_state.token
)

if response.status_code != 200:

    st.error("Unable to fetch AI Matches.")

    st.stop()

matches = response.json()

if len(matches) == 0:

    st.info("No Matches Found.")

    st.stop()

for match in matches:

    score = match.get("match_score", 0)

    if score >= 90:
        color = "🟢"
    elif score >= 75:
        color = "🟡"
    else:
        color = "🔴"

    with st.container(border=True):

        c1, c2 = st.columns([4,1])

        with c1:

            st.subheader(match["listing_title"])

            st.write(f"📍 {match['location']}")

            st.write(f"💰 ₹ {match['rent']}")

            st.write(f"🏠 {match['property_type']}")

            st.progress(score/100)

            st.success(
                f"{color} Compatibility Score : {score}%"
            )

            st.markdown("### 🧠 AI Explanation")

            st.write(match["reason"])

            st.markdown("### Lifestyle")

            st.write(f"🍽 Food : {match['food_preference']}")

            st.write(f"🚭 Smoking : {match['smoking_allowed']}")

            st.write(f"🍺 Drinking : {match['drinking_allowed']}")

            st.write(f"🐶 Pets : {match['pets_allowed']}")

        with c2:

            if st.button(
                "❤️ Interested",
                key=match["listing_id"]
            ):

                interest = send_interest(
                    st.session_state.token,
                    match["listing_id"]
                )

                if interest.status_code in [200,201]:

                    st.success("Interest Sent")

                else:

                    st.error("Already Sent")

            st.metric(
                "Score",
                f"{score}%"
            )

        st.divider()