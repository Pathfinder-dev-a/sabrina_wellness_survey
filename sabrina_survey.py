import streamlit as st
import pandas as pd
import datetime
import os

st.set_page_config(page_title="Sabrina Wellness Survey", page_icon="🪶")

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

# Save to CSV
if st.button("✅ Submit Survey"):
    new_entry = pd.DataFrame([{
        "Name": name,
        "Date": date,
        "Mental Clarity": clarity,
        "Overthinking": overthinking,
        "Emotional State": feeling,
        "Support Felt": support,
        "Sleep Quality": sleep,
        "Energy Level": energy,
        "Pain Present": pain,
        "Land Connection": land,
        "Gratitude": gratitude,
        "Reflection": reflection
    }])

    file_path = "sabrina_responses.csv"
    if os.path.exists(file_path):
        existing = pd.read_csv(file_path)
        updated = pd.concat([existing, new_entry], ignore_index=True)
    else:
        updated = new_entry

    updated.to_csv(file_path, index=False)
    st.success("🌿 Your response has been saved.")
    st.balloons()

st.markdown("---")
st.markdown("*“The land knows you, even when you are lost.” – Cree Elder*")
