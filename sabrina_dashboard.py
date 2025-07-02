import streamlit as st
import pandas as pd

st.set_page_config(page_title="Sabrina Wellness Dashboard", page_icon="📊", layout="wide")

st.title("📊 Sabrina Wellness Dashboard")
st.markdown("Real-time visualization of community wellness using the **Medicine Wheel** as a guide.")

# Load data
file_path = "sabrina_responses.csv"
try:
    df = pd.read_csv(file_path, parse_dates=["Date"])
    df["Date"] = pd.to_datetime(df["Date"])
except FileNotFoundError:
    st.warning("⚠️ No survey data found yet. Submit some responses to begin.")
    st.stop()

# Sidebar filters
st.sidebar.header("🔍 Filter Responses")
name_filter = st.sidebar.selectbox("Select Name (or All)", ["All"] + sorted(df["Name"].dropna().unique().tolist()))
if name_filter != "All":
    df = df[df["Name"] == name_filter]

# Quadrants
st.markdown("## 🧭 Medicine Wheel Domains")

col1, col2 = st.columns(2)

with col1:
    st.subheader("🧠 Mental (North - White)")
    st.metric("Average Mental Clarity", round(df["Mental Clarity"].mean(), 1))
    st.bar_chart(df.groupby("Date")["Mental Clarity"].mean())

    st.write("**Overthinking Trends:**")
    st.line_chart(df["Overthinking"].value_counts(normalize=True))

with col2:
    st.subheader("❤️ Emotional (South - Red)")
    emotional_counts = df["Emotional State"].value_counts()
    st.write("**Emotional Check-ins:**")
    st.bar_chart(emotional_counts)

    support_counts = df["Support Felt"].value_counts()
    st.write("**Support Felt:**")
    st.bar_chart(support_counts)

st.markdown("---")

col3, col4 = st.columns(2)

with col3:
    st.subheader("💪 Physical (West - Black)")
    st.metric("Avg Sleep Quality", round(df["Sleep Quality"].mean(), 1))
    st.metric("Avg Energy Level", round(df["Energy Level"].mean(), 1))

    st.write("**Pain Reports:**")
    pain_data = df["Pain Present"].value_counts()
    st.bar_chart(pain_data)

with col4:
    st.subheader("🌱 Spiritual (East - Yellow)")
    land_counts = df["Land Connection"].value_counts()
    st.write("**Land Connection Check-ins:**")
    st.bar_chart(land_counts)

    st.write("**Gratitude Examples:**")
    for i, entry in df["Gratitude"].dropna().sample(min(3, len(df))).items():
        st.markdown(f"- {entry}")

# Final reflections
if st.checkbox("Show Reflections"):
    st.subheader("💬 Final Reflections")
    for i, entry in df["Reflection"].dropna().items():
        st.markdown(f"🪶 *{entry}*")

st.markdown("---")
st.caption("Medicine Wheel © All Nations · This dashboard is grounded in Indigenous wellness teachings.")
