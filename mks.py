# ======================================================

st.markdown("---")
st.subheader("🧠 IPL Quiz 3")

answer3 = st.radio(
    "Which bowler has taken the most wickets in IPL history?",
    [
        "Jasprit Bumrah",
        "Yuzvendra Chahal",
        "Lasith Malinga",
        "Bhuvneshwar Kumar"
    ],
    key="quiz3"
)

if st.button("Submit Quiz 3"):

    if answer3 == "Yuzvendra Chahal":
        st.success("✅ Correct Answer!")
        st.balloons()
    else:
        st.error("❌ Wrong Answer. Correct Answer: Yuzvendra Chahal")

st.success("✅ Thanks for Exploring IPL Pro Analytics Hub")
# ======================================================
# 📊 PANDAS DATA ANALYSIS SECTION
# ======================================================

import pandas as pd

st.markdown("---")
st.header("📊 Data Science Analysis using Pandas")

# Create DataFrame
df = pd.DataFrame(all_players)

# Show Complete Dataset
st.subheader("📋 Complete IPL Player Dataset")
st.dataframe(df, use_container_width=True)

# ======================================================
# Top 10 Run Scorers
# ======================================================

st.markdown("---")
st.subheader("🏏 Top 10 Run Scorers")

top_runs = df.sort_values(by="Runs", ascending=False).head(10)

st.dataframe(
    top_runs[["Player", "Team", "Runs", "Matches"]],
    use_container_width=True
)

# ======================================================
# Top 10 Wicket Takers
# ======================================================

st.markdown("---")
st.subheader("🎯 Top 10 Wicket Takers")

top_wickets = df.sort_values(by="Wickets", ascending=False).head(10)

st.dataframe(
    top_wickets[["Player", "Team", "Wickets", "Matches"]],
    use_container_width=True
)

# ======================================================
# Team-wise Summary
# ======================================================

st.markdown("---")
st.subheader("🏆 Team-wise Statistics")

team_summary = df.groupby("Team")[["Runs", "Wickets", "Matches"]].sum().reset_index()

st.dataframe(team_summary, use_container_width=True)

# ======================================================
# Basic Statistics
# ======================================================

st.markdown("---")
st.subheader("📈 Statistical Summary")

st.dataframe(df.describe(), use_container_width=True)

# ======================================================
# CSV Download
# ======================================================

st.markdown("---")
st.subheader("⬇ Download Dataset")

csv = df.to_csv(index=False)

st.download_button(
    label="📥 Download IPL Dataset",
    data=csv,
    file_name="IPL_Player_Data.csv",
    mime="text/csv"
)
