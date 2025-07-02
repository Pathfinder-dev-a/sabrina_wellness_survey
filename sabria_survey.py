import streamlit as st
import pandas as pd
import datetime
import os

# Setup
st.set_page_config(page_title="Sabria Wellness Survey", page_icon="🪶")
st.title("🪶 Sabria Wellness Survey")
st.markdown("Track your well-being using Indigenous knowledge systems and personal reflection.")

# Collect user data
name = st.text_input("👤 Your Name:")
date = st.date_input("📅 Date", datetime.date.today())

st.markdown("## 🧭 Medicine Wheel Check-In")

# Medicine Wheel categories
with st.expander("🧠 Mental"):
    clarity = st.slider("Mental Clarity (0 = foggy, 10 = focused)", 0, 10, 5)
    overthinking = st.checkbox("Feeling overwhelmed or overthinking?")

with st.expander("❤️ Emotional"):
    feeling = st.radio("Emotion check-in:", ["Joyful", "Calm", "Anxious", "Sad", "Numb"])
    support = st.selectbox("Do you feel emotionally supported?", ["Yes", "Somewhat", "No"])

with st.expander("💪 Physical"):
    sleep = st.slider("How well did you sleep last night?", 0, 10, 5)
    energy = st.slider("Physical energy level", 0, 10, 5)
    pain = st.checkbox("Experiencing pain or discomfort?")

with st.expander("🌱 Spiritual"):
    land = st.selectbox("Have you connected with land today?", ["Yes", "No", "Not sure"])
    gratitude = st.text_area("What are you grateful for today?")

st.markdown("## 💬 Final Reflections")
reflection = st.text_area("Optional reflections, teachings, dreams, visions...")

# Save response
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

    file_path = "sabria_responses.csv"

    if os.path.exists(file_path):
        existing = pd.read_csv(file_path)
        updated = pd.concat([existing, new_entry], ignore_index=True)
    else:
        updated = new_entry

    updated.to_csv(file_path, index=False)
    st.success("🌿 Your response has been saved. Thank you!")
    st.balloons()

# Optional quote
st.markdown("---")
st.markdown("*“The land knows you, even when you are lost.” – Cree Elder*")
