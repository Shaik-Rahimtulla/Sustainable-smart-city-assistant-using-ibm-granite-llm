import streamlit as st
import requests
from cities_list import cities

def govt_schemes_ui():
    st.subheader("🧾 Govt Scheme Advisor")
    city = st.selectbox("Select city", cities, key="govt")
    target = st.selectbox("Choose target group", ["women", "students", "farmers", "senior citizens"])
    if st.button("Get Schemes"):
        res = requests.post("http://localhost:8000/govt_schemes", data={"city": city, "target": target})
        st.success(res.json()["response"])
