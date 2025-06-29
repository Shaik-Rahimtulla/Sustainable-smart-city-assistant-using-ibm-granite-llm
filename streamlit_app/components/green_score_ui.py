import streamlit as st
import requests
from cities_list import cities

def green_score_ui():
    st.subheader("🌿 Green Score – Evaluate a city's eco-friendliness")
    city = st.selectbox("Select city", cities, key="green")
    if st.button("Get Green Score"):
        res = requests.post("http://localhost:8000/green_score", data={"city": city})
        st.success(res.json()["response"])
