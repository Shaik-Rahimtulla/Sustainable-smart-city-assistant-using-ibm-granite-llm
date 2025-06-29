import streamlit as st
import requests

def summarizer_ui():
    st.subheader("📄 Document Summarizer – Upload PDFs for Summary")
    file = st.file_uploader("Upload a PDF file", type=["pdf"])
    if st.button("Summarize") and file:
        files = {"file": file.getvalue()}
        res = requests.post("http://localhost:8000/summarize", files={"file": file})
        st.success(res.json()["response"])
