import streamlit as st
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Page config
st.set_page_config(page_title="Sabrina Wellness Dashboard", page_icon="📊", layout="wide")

# Google Sheets auth
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds_dict = st.secrets["gcp_service"]
creds = ServiceAccountCredentials.from_json_keyfile_dict(dict(creds_dict), scope)
client = gspread.authorize(creds)
sheet = client.open("Sabrina Wellness Responses").sheet1

# Load sheet data
data = sheet.get_all_records()
if not data:
    st.warning("⚠️ No survey data available.")
    st.stop()

df = pd.DataFrame(data)
df["Date"] = pd.to_datetime(df["Date"])

st.title("📊 Sabrina Wellness Dashboard")
st.markdown("Visualizing wellness data with the guidance of the Medicine Wheel.")

# Filter by name
names = ["All"] + sorted(df["Name"].dropna().unique().tolist())
selected_name = st.sidebar.selectbox("🔎 Filter by Name", names)
if selected_name != "All":
    df = df[df["Name"] == selected_name]

# Quadrant visuals
col1, col2 = st.columns(2)

with col1:
    st.subheader("🧠 Mental (North - White)")
    st.metric("Avg Mental Clarity", round(df["Mental Clarity"].mean(), 1))
    st.bar_chart(df.groupby("Date")["Mental Clarity"].mean())

    st.write("**Overthinking Trends:**")
    overthink_count = df["Overthinking"].value_counts()
    st.bar_chart(overthink_count)

with col2:
    st.subheader("❤️ Emotional (South - Red)")
    emo_counts = df["Emotional State"].value_counts()
    st.bar_chart(emo_counts)

    support_counts = df["Support Felt"].value_counts()
    st.write("**Support Felt:**")
    st.bar_chart(support_counts)

col3, col4 = st.columns(2)

with col3:
    st.subheader("💪 Physical (West - Black)")
    st.metric("Avg Sleep Quality", round(df["Sleep Quality"].mean(), 1))
    st.metric("Avg Energy Level", round(df["Energy Level"].mean(), 1))
    pain_counts = df["Pain Present"].value_counts()
    st.write("**Pain Reports:**")
    st.bar_chart(pain_counts)

with col4:
    st.subheader("🌱 Spiritual (East - Yellow)")
    land_counts = df["Land Connection"].value_counts()
    st.write("**Land Connection:**")
    st.bar_chart(land_counts)

    st.write("**Gratitude Examples:**")
    for i, entry in df["Gratitude"].dropna().sample(min(3, len(df))).items():
        st.markdown(f"- {entry}")

# Final reflections
if st.checkbox("Show Final Reflections"):
    st.subheader("💬 Final Reflections")
    for i, entry in df["Reflection"].dropna().items():
        st.markdown(f"🪶 *{entry}*")

st.markdown("---")
st.caption("This dashboard uses the Medicine Wheel as a sacred guide for healing and balance.")
