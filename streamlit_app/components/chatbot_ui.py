import streamlit as st
import requests

def chatbot_ui():
    st.subheader("💬 Chat Assistant – Ask anything about the city")
    question = st.text_input("Your question")
    if st.button("Ask"):
        res = requests.post("http://localhost:8000/chat", data={"question": question})
        st.success(res.json()["response"])
