import streamlit as st
import pandas as pd
import datetime, os

st.set_page_config(page_title="Sabria Wellness Survey", page_icon="🪶")
st.title("🪶 Sabria Wellness Survey")
st.markdown("Click on each quadrant of the Medicine Wheel to complete that section. All 4 are required 📋")

# Session state setup
if 'done' not in st.session_state:
    st.session_state.done = {q: False for q in ["Mental","Emotional","Physical","Spiritual"]}
    st.session_state.data = {}

# Display image
st.image("medicine_wheel.png", use_column_width=True)

# Quadrant click simulation
cols = st.columns(2)
if cols[0].button("🧠 Mental"):
    st.session_state.active = "Mental"
if cols[0].button("💪 Physical"):
    st.session_state.active = "Physical"
if cols[1].button("❤️ Emotional"):
    st.session_state.active = "Emotional"
if cols[1].button("🌱 Spiritual"):
    st.session_state.active = "Spiritual"

# Collect name and date once
if 'name' not in st.session_state:
    st.session_state.name = st.text_input("Your Name")
    st.session_state.date = st.date_input("Date", datetime.date.today())

# Show quadrant questions when clicked
quad = st.session_state.get("active", None)
if quad:
    st.subheader(f"{quad} Check-In")
    if quad == "Mental":
        clarity = st.slider("Clarity (0‑10)", 0, 10, 5, key="clarity")
        over = st.checkbox("Overthinking?", key="over")
        st.session_state.data["Mental"] = {"Mental Clarity": clarity, "Overthinking": over}
    elif quad == "Emotional":
        emo = st.radio("Emotion", ["Joyful","Calm","Anxious","Sad","Numb"], key="emo")
        sup = st.selectbox("Supported?", ["Yes","Somewhat","No"], key="sup")
        st.session_state.data["Emotional"] = {"Emotion": emo, "Support": sup}
    elif quad == "Physical":
        sleep = st.slider("Sleep (0‑10)", 0, 10, 5, key="sleep")
        ener = st.slider("Energy (0‑10)", 0, 10, 5, key="ener")
        pain = st.checkbox("In pain?", key="pain")
        st.session_state.data["Physical"] = {"Sleep": sleep, "Energy": ener, "Pain": pain}
    else:
        land = st.selectbox("Land today?", ["Yes","No","Not sure"], key="land")
        grat = st.text_area("Grateful for...", key="grat")
        st.session_state.data["Spiritual"] = {"Land": land, "Gratitude": grat}

    if st.button(f"✔️ Finish {quad}"):
        st.session_state.done[quad] = True
        st.success(f"{quad} section completed!")
        st.session_state.active = None

# Check if all 4 done
if all(st.session_state.done.values()):
    reflection = st.text_area("💬 Final reflections?")
    if st.button("✅ Submit Full Survey"):
        # compile
        entry = {"Name": st.session_state.name, "Date": st.session_state.date}
        for q, vals in st.session_state.data.items():
            entry.update(vals)
        entry["Reflection"] = reflection
        df = pd.DataFrame([entry])
        path = "sabria_responses.csv"
        if os.path.exists(path):
            df = pd.concat([pd.read_csv(path), df], ignore_index=True)
        df.to_csv(path, index=False)
        st.success("🌿 Survey saved! Thanks!")
        st.balloons()
        st.session_state.done = {q: False for q in st.session_state.done}
        st.session_state.data.clear()
