
import streamlit as st

# === Language Setup ===
languages = {
    "English": "en",
    "Tiếng Việt": "vi",
    "繁體中文": "zh"
}

lang = st.selectbox("🌐 Select Language / Chọn ngôn ngữ / 選擇語言", list(languages.keys()))
lang_code = languages[lang]

# === Translation Dictionary ===
t = {
    "research_tab": {"en": "🔬 Research Boosts", "vi": "🔬 Tăng Cường Nghiên Cứu", "zh": "🔬 科研加成"},
    "duel_tab": {"en": "📆 VS Duel Day", "vi": "📆 Ngày Đấu VS", "zh": "📆 對決日"},
    "select_day": {"en": "📅 Choose Day", "vi": "📅 Chọn Ngày", "zh": "📅 選擇日子"},
    "boost_level": {"en": "Research Level", "vi": "Cấp Nghiên Cứu", "zh": "研究等級"},
    "saved_msg": {"en": "All research boosts saved. Go to next tab to calculate score!",
                  "vi": "Đã lưu tăng cường nghiên cứu. Chuyển sang tab tiếp theo để tính điểm!",
                  "zh": "研究加成已儲存。請切換分頁進行計算！"},
    "task_label": {"en": "Tasks for", "vi": "Nhiệm vụ cho", "zh": "任務 -"},
    "points_label": {"en": "points", "vi": "điểm", "zh": "分數"},
    "total_label": {"en": "🏆 Total Score for", "vi": "🏆 Tổng điểm cho", "zh": "🏆 總分 -"}
}

# === VS Duel Day Data ===
vs_duel_days_data = {
    "Monday - Radar Training": {
        "Complete 1 radar task": 25000,
        "Use 1 Stamina": 300,
        "Use 660 Hero EXP Points": 2,
        "Use 10pts of Drone Battle Data": 6,
        "Use 1 drone part": 5000,
        "Gather 100 food": 30,
        "Gather 100 Iron": 40,
        "Gather 60 Coins": 40
    },
    "Tuesday - Base Expansion": {
        "Use 1-min Construction Speedup": 125,
        "Increasse Building power": 25,
        "Dispatch Legendary Trade Truck": 200000,
        "Perform Legendary Secret Task": 150000
    },
    "Wednesday - Age of Science": {
        "Use 1-min Research Speedup": 125,
        "Increase Tech Power": 25,
        "Use 1 Valor badge": 600,
        "Complete 1 radar Task": 25000
    },
    "Thursday - Train Heroes": {
        "Elite Recruit 1 time": 3750,
        "Use 2.000 Hero EXP Points": 6,
        "Use Legendary Hero Shard": 20000,
        "Use Epic Hero Shard": 7500,
        "Use Rare Hero Shard": 2000,
        "Use 1 Skill Medal": 20
    },
    "Friday - Total Mobilization": {
        "Complete 1 radar task": 22500,
        "Use 1-min Construction Speedup": 112,
        "Increasse Building power": 19,
        "Use 1-min Research Speedup": 112,
        "Increase Tech Power": 19,
        "Use 1-min Training Speedup": 112,
        "Train a lvl 1 unit": 40,
        "Train a lvl 2 unit": 60,
        "Train a lvl 3 unit": 80,
        "Train a lvl 4 unit": 100,
        "Train a lvl 5 unit": 120,
        "Train a lvl 6 unit": 140,
        "Train a lvl 7 unit": 160,
        "Train a lvl 8 unit": 180,
        "Train a lvl 9 unit": 200,
        "Train a lvl 10 unit": 220
    },
    "Saturday - Enemy Buster": {
        "Dispatch Legendary Trade Truck": 175000,
        "Perform Legendary Secret Task": 131250,
        "Use 1-min Construction Speedup": 112,
        "Use 1-min Research Speedup": 112,
        "Use 1-min Training Speedup": 112,
        "Use 1-min Healing Speedup": 112,
        "Killed lvl 1 unit from rival": 19,
        "Killed lvl 2 unit from rival": 29,
        "Killed lvl 3 unit from rival": 39,
        "Killed lvl 4 unit from rival": 48,
        "Killed lvl 5 unit from rival": 58,
        "Killed lvl 6 unit from rival": 68,
        "Killed lvl 7 unit from rival": 47,
        "Killed lvl 8 unit from rival": 87,
        "Killed lvl 9 unit from rival": 97,
        "Killed lvl 10 unit from rival": 107,
        "Killed lvl 1 unit": 3,
        "Killed lvl 2 unit": 5,
        "Killed lvl 3 unit": 7,
        "Killed lvl 4 unit": 9,
        "Killed lvl 5 unit": 11,
        "Killed lvl 6 unit": 13,
        "Killed lvl 7 unit": 15,
        "Killed lvl 8 unit": 17,
        "Killed lvl 9 unit": 19,
        "Killed lvl 10 unit": 21,
        "Every lvl 1 unit lost": 3,
        "Every lvl 2 unit lost": 5,
        "Every lvl 3 unit lost": 7,
        "Every lvl 4 unit lost": 8,
        "Every lvl 5 unit lost": 10,
        "Every lvl 6 unit lost": 12,
        "Every lvl 7 unit lost": 14,
        "Every lvl 8 unit lost": 15,
        "Every lvl 9 unit lost": 17,
        "Every lvl 10 unit lost": 19
    }
}

task_to_research = {
    "Complete 1 radar task": "Radar", "Complete 1 radar Task": "Radar",
    "Use 1-min Construction Speedup": "Speed-Up", "Use 1-min Research Speedup": "Speed-Up",
    "Use 1-min Training Speedup": "Speed-Up", "Use 1-min Healing Speedup": "Speed-Up",
    "Increasse Building power": "Building", "Increase Tech Power": "Research",
    "Train a lvl 1 unit": "Training", "Train a lvl 2 unit": "Training", "Train a lvl 3 unit": "Training",
    "Train a lvl 4 unit": "Training", "Train a lvl 5 unit": "Training", "Train a lvl 6 unit": "Training",
    "Train a lvl 7 unit": "Training", "Train a lvl 8 unit": "Training", "Train a lvl 9 unit": "Training",
    "Train a lvl 10 unit": "Training", "Elite Recruit 1 time": "Recruitment",
    "Killed lvl 1 unit from rival": "Enemy Kills", "Killed lvl 2 unit from rival": "Enemy Kills",
    "Killed lvl 3 unit from rival": "Enemy Kills", "Killed lvl 4 unit from rival": "Enemy Kills",
    "Killed lvl 5 unit from rival": "Enemy Kills", "Killed lvl 6 unit from rival": "Enemy Kills",
    "Killed lvl 7 unit from rival": "Enemy Kills", "Killed lvl 8 unit from rival": "Enemy Kills",
    "Killed lvl 9 unit from rival": "Enemy Kills", "Killed lvl 10 unit from rival": "Enemy Kills"
}

st.set_page_config(page_title="VS Duel Calculator", layout="centered")

tab1, tab2 = st.tabs([t["research_tab"][lang_code], t["duel_tab"][lang_code]])

research_types = [
    "Radar", "Speed-Up", "Duel Expert", "Building",
    "Research", "Training", "Recruitment", "Enemy Kills"
]

if "research_levels" not in st.session_state:
    st.session_state.research_levels = {r: 0 for r in research_types}

with tab1:
    st.header(t["research_tab"][lang_code])
    for r in research_types:
        st.session_state.research_levels[r] = st.selectbox(
            f"{r} {t['boost_level'][lang_code]}",
            list(range(0, 11)),
            index=st.session_state.research_levels[r],
            key=f"research_{r}"
        )
    st.success(t["saved_msg"][lang_code])

with tab2:
    st.header(t["duel_tab"][lang_code])
    day_selected = st.selectbox(t["select_day"][lang_code], list(vs_duel_days_data.keys()))
    tasks = vs_duel_days_data[day_selected]

    total_score = 0
    st.subheader(f"{t['task_label'][lang_code]} {day_selected}")
    for task, base_points in tasks.items():
        input_key = f"{day_selected}_{task}_input"
        qty = st.number_input(f"{task}", min_value=0, value=0, step=1, key=input_key)

        boost_pct = 0
        if task in task_to_research:
            boost_pct += st.session_state.research_levels.get(task_to_research[task], 0) * 5
        boost_pct += st.session_state.research_levels["Duel Expert"] * 5

        points = qty * base_points * (1 + boost_pct / 100)
        total_score += points

        st.write(f"→ {int(points):,} {t['points_label'][lang_code]} (Base: {base_points} × Qty: {qty} × Boost: +{boost_pct}%)")

    st.success(f"{t['total_label'][lang_code]} {day_selected}: {int(total_score):,} {t['points_label'][lang_code]}")
