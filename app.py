
import streamlit as st

st.set_page_config(page_title="VS Duel Calculator", layout="centered")

# Language options
languages = {
    "English": "en",
    "Tiếng Việt": "vi",
    "繁體中文": "zh"
}

lang_choice = st.selectbox("🌐 Select Language / Chọn ngôn ngữ / 選擇語言", list(languages.keys()))
lang = languages[lang_choice]

# Translations
text = {
    "tabs": {
        "research": {
            "en": "🔬 Research Levels",
            "vi": "🔬 Cấp Nghiên Cứu",
            "zh": "🔬 科研等級"
        },
        "vs_day": {
            "en": "📆 VS Duel Day",
            "vi": "📆 Ngày VS",
            "zh": "📆 VS對決日"
        }
    },
    "radar_day": {
        "en": "Monday - Radar Day",
        "vi": "Thứ Hai - Ngày Radar",
        "zh": "星期一 - 雷達日"
    },
    "construction_day": {
        "en": "Tuesday - Construction Day",
        "vi": "Thứ Ba - Ngày Xây Dựng",
        "zh": "星期二 - 建設日"
    }
}

# Tabs for navigation
tab1, tab2 = st.tabs([text["tabs"]["research"][lang], text["tabs"]["vs_day"][lang]])

# Research multipliers storage
if "research_boosts" not in st.session_state:
    st.session_state.research_boosts = {
        "Radar Task": 0,
        "Construction Power": 0
    }

# Tab 1: Research Levels
with tab1:
    st.header(text["tabs"]["research"][lang])

    radar_level = st.selectbox("Radar Research Level (affects Radar Tasks)", list(range(0, 11)), index=0)
    construction_level = st.selectbox("Construction Research Level (affects Building Power)", list(range(0, 11)), index=0)

    st.session_state.research_boosts["Radar Task"] = radar_level * 5  # +5% per level
    st.session_state.research_boosts["Construction Power"] = construction_level * 3  # +3% per level

    st.success(f"Radar Task Bonus: +{st.session_state.research_boosts['Radar Task']}%")
    st.success(f"Construction Power Bonus: +{st.session_state.research_boosts['Construction Power']}%")

# Tab 2: VS Duel Day
with tab2:
    st.header(text["tabs"]["vs_day"][lang])

    day = st.selectbox("Select Day", [
        text["radar_day"][lang],
        text["construction_day"][lang]
    ])

    if day == text["radar_day"][lang]:
        st.subheader(text["radar_day"][lang])
        stamina_used = st.number_input("Stamina Used", min_value=0, value=0)
        radar_tasks = st.number_input("Radar Tasks Completed", min_value=0, value=0)

        stamina_points = stamina_used * 375
        radar_base = radar_tasks * 30000
        radar_bonus = radar_base * (st.session_state.research_boosts["Radar Task"] / 100)
        radar_total = radar_base + radar_bonus

        total_score = stamina_points + radar_total

        st.metric("Total Radar Day Score", f"{total_score:,.0f} points")
        st.caption(f"Includes +{st.session_state.research_boosts['Radar Task']}% bonus on Radar Tasks")

    elif day == text["construction_day"][lang]:
        st.subheader(text["construction_day"][lang])
        speedup_minutes = st.number_input("Construction Speedups Used (in minutes)", min_value=0, value=0)
        power_increase = st.number_input("Building Power Increased", min_value=0, value=0)

        speedup_points = speedup_minutes * 125
        construction_base = power_increase * 23
        construction_bonus = construction_base * (st.session_state.research_boosts["Construction Power"] / 100)
        construction_total = construction_base + construction_bonus

        total_score = speedup_points + construction_total

        st.metric("Total Construction Day Score", f"{total_score:,.0f} points")
        st.caption(f"Includes +{st.session_state.research_boosts['Construction Power']}% bonus on Building Power")
