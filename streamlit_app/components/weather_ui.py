import streamlit as st
import requests
from cities_list import cities

def weather_ui():
    st.subheader("🌤️ Weather Info – Get today's weather")
    city = st.selectbox("Choose a city", cities, key="weather")
    if st.button("Show Weather"):
        res = requests.post("http://localhost:8000/weather", data={"city": city})
        st.success(res.json()["response"])
