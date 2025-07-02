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

    try:
        existing = pd.read_csv(file_path)
        updated = pd.concat([existing, new_entry], ignore_index=True)
    except FileNotFoundError:
        updated = new_entry  # first time run, no file exists

    updated.to_csv(file_path, index=False)
    st.success("🌿 Your response has been saved.")
    st.balloons()
