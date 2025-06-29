import streamlit as st
import requests
from cities_list import cities

def city_policy_ui():
    st.subheader("🏛️ City Policy & Schemes – Health, Education, Housing, etc.")
    city = st.selectbox("Choose a city", cities)
    topic = st.text_input("Enter topic (e.g., health, education, housing)")
    if st.button("Get Policies"):
        res = requests.post("http://localhost:8000/city_policies", data={"city": city, "topic": topic})
        st.success(res.json()["response"])
