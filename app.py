
import streamlit as st

st.set_page_config(page_title="VS Duel Calculator", layout="centered")

# Placeholder for research level boosts
research_boosts = {
    "Radar Task": 0,
    "Construction Power": 0
}

# Sidebar for selecting section
section = st.sidebar.radio("Select Section", ["🔬 Research Levels", "📆 VS Duel Day"])

# Section 1: Research Levels Input
if section == "🔬 Research Levels":
    st.title("Research Boost Levels")
    st.markdown("Set your current research level boosts for each VS Duel task type.")

    radar_level = st.slider("Radar Research Level (affects Radar Tasks)", 0, 10, 0)
    construction_level = st.slider("Construction Research Level (affects Building Power)", 0, 10, 0)

    # Use placeholder multiplier per level for now
    research_boosts["Radar Task"] = radar_level * 5  # 5% per level
    research_boosts["Construction Power"] = construction_level * 3  # 3% per level

    st.info(f"Radar Task bonus: +{research_boosts['Radar Task']}%")
    st.info(f"Construction Power bonus: +{research_boosts['Construction Power']}%")

# Section 2: VS Duel Day
elif section == "📆 VS Duel Day":
    st.title("VS Duel Day Scoring Calculator")

    day = st.selectbox("Select Day", ["Monday - Radar Day", "Tuesday - Construction Day"])

    if day.startswith("Monday"):
        st.header("Radar Day")
        stamina_used = st.number_input("Stamina Used", min_value=0, value=0)
        radar_tasks = st.number_input("Radar Tasks Completed", min_value=0, value=0)

        stamina_points = stamina_used * 375
        radar_base = radar_tasks * 30000
        radar_bonus = radar_base * (research_boosts["Radar Task"] / 100)
        radar_total = radar_base + radar_bonus

        total_score = stamina_points + radar_total

        st.metric("Total Radar Day Score", f"{total_score:,.0f} points")
        st.caption(f"Includes +{research_boosts['Radar Task']}% bonus on Radar Tasks")

    elif day.startswith("Tuesday"):
        st.header("Construction Day")
        speedup_minutes = st.number_input("Construction Speedups Used (in minutes)", min_value=0, value=0)
        power_increase = st.number_input("Building Power Increased", min_value=0, value=0)

        speedup_points = speedup_minutes * 125
        construction_base = power_increase * 23
        construction_bonus = construction_base * (research_boosts["Construction Power"] / 100)
        construction_total = construction_base + construction_bonus

        total_score = speedup_points + construction_total

        st.metric("Total Construction Day Score", f"{total_score:,.0f} points")
        st.caption(f"Includes +{research_boosts['Construction Power']}% bonus on Building Power")

