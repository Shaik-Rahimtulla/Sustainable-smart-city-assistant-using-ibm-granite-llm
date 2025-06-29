import streamlit as st
from components.city_policy_ui import city_policy_ui
from components.eco_tips_ui import eco_tips_ui
from components.summarizer_ui import summarizer_ui
from components.chatbot_ui import chatbot_ui
from components.green_score_ui import green_score_ui
from components.govt_schemes_ui import govt_schemes_ui
from components.events_alerts_ui import events_alerts_ui
from components.public_transport_ui import public_transport_ui
from components.weather_ui import weather_ui

st.set_page_config(page_title="Sustainable Smart City Assistant", layout="centered")

st.title("🌆 Sustainable Smart City Assistant using IBM Granite LLM")
st.markdown("### Select any feature below:")

features = {
    "City Policy & Schemes": city_policy_ui,
    "Eco Tips Generator": eco_tips_ui,
    "Document Summarizer": summarizer_ui,
    "Chat Assistant": chatbot_ui,
    "Events & Alerts": events_alerts_ui,
    "Govt Schemes": govt_schemes_ui,
    "Green Score": green_score_ui,
    "Public Transport Assistant": public_transport_ui,
    "Weather Info": weather_ui
}

selected = st.multiselect("Select Features", list(features.keys()))

for feature in selected:
    features[feature]()  # Call the respective UI
