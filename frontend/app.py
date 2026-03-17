import streamlit as st
import requests

st.title("Clinical AI Assistant - Day 1")

uploaded_file = st.file_uploader("Upload Patient Report", type=["txt", "pdf"])

if uploaded_file is not None:
    files = {"file": uploaded_file.getvalue()}

    response = requests.post(
        "http://127.0.0.1:8000/process",
        files={"file": (uploaded_file.name, uploaded_file.getvalue())}
    )

    if response.status_code == 200:
        data = response.json()

        st.subheader("Raw Text")
        st.write(data["raw_text"])

        st.subheader("Extracted Information")
        st.json(data["extracted"])