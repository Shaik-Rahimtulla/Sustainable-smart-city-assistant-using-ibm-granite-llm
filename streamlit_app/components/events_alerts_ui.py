import streamlit as st
import requests
from cities_list import cities

def events_alerts_ui():
    st.subheader("🗓️ Events & Alerts – View upcoming city events")
    city = st.selectbox("Select city", cities, key="events")
    if st.button("Get Events"):
        res = requests.post("http://localhost:8000/events_alerts", data={"city": city})
        st.success(res.json()["response"])
