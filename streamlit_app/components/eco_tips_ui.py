import streamlit as st
import requests

def eco_tips_ui():
    st.subheader("🌱 Eco Tips Generator – Water, Air, Animals, Trees, etc.")
    problem = st.text_input("Enter a problem (e.g., air pollution, water pollution)")
    if st.button("Generate Tips"):
        res = requests.post("http://localhost:8000/eco_tips", data={"problem": problem})
        st.success(res.json()["response"])
