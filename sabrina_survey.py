import streamlit as st
import pandas as pd
import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Configure page
st.set_page_config(page_title="Sabrina Wellness Survey", page_icon="🪶")

# Setup credentials from Streamlit Secrets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds_dict = st.secrets["gcp_service"]
creds = ServiceAccountCredentials.from_json_keyfile_dict(dict(creds_dict), scope)
client = gspread.authorize(creds)
sheet = client.open("Sabrina Wellness Responses").sheet1

# App content
st.title("🪶 Sabrina Wellness Survey")
st.markdown("Track your well-being using Indigenous knowledge systems and personal reflection.")

name = st.text_input("👤 Your Name:")
date = st.date_input("📅 Date", datetime.date.today())

st.markdown("## 🧭 Medicine Wheel Check-In")

with st.expander("🧠 Mental (North - White)"):
    clarity = st.slider("Mental Clarity (0 = foggy, 10 = focused)", 0, 10, 5)
    overthinking = st.checkbox("Feeling overwhelmed or overthinking?")

with st.expander("❤️ Emotional (South - Red)"):
    feeling = st.radio("Emotional State:", ["Joyful", "Calm", "Anxious", "Sad", "Numb"])
    support = st.selectbox("Do you feel emotionally supported?", ["Yes", "Somewhat", "No"])

with st.expander("💪 Physical (West - Black)"):
    sleep = st.slider("Sleep Quality", 0, 10, 5)
    energy = st.slider("Energy Level", 0, 10, 5)
    pain = st.checkbox("Experiencing pain or discomfort?")

with st.expander("🌱 Spiritual (East - Yellow)"):
    land = st.selectbox("Connected with the land today?", ["Yes", "No", "Not sure"])
    gratitude = st.text_area("What are you grateful for today?")

st.markdown("## 💬 Final Reflections")
reflection = st.text_area("Optional reflections, teachings, or dreams...")

if st.button("✅ Submit Survey"):
    new_row = [
        name,
        str(date),
        clarity,
        str(overthinking),
        feeling,
        support,
        sleep,
        energy,
        str(pain),
        land,
        gratitude,
        reflection,
    ]
    sheet.append_row(new_row)
    st.success("🌿 Your response has been saved to Google Sheets.")
    st.balloons()

st.markdown("---")
st.markdown("*“The land knows you, even when you are lost.” – Cree Elder*")
