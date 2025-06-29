import streamlit as st
import requests
from cities_list import cities

def public_transport_ui():
    st.subheader("🚍 Public Transport Assistant")
    city = st.selectbox("Select city", cities, key="transport")
    if st.button("Show Transport Info"):
        res = requests.post("http://localhost:8000/public_transport", data={"city": city})
        st.success(res.json()["response"])
