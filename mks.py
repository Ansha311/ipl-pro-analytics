import streamlit as st
import os
import time
from datetime import datetime

# 1. Page Configuration Set Up
st.set_page_config(page_title="IPL Pro Analytics Hub", page_icon="🏏", layout="wide")

# 2. Embedded Premium Dark CSS with Dynamic Animated Stars Background (Fixed No-Freeze)
st.markdown("""
<style>
/* Base Theme backdrop setup */
.stApp {
    background: radial-gradient(ellipse at bottom, #1b2735 0%, #090a0f 100%) !important;
    background-attachment: fixed !important;
}

/* Dynamic CSS Star Generation Framework */
.stApp::before {
    content: " ";
    position: fixed;
    top: 0; left: 0; width: 3px; height: 3px;
    border-radius: 50%; z-index: 0; pointer-events: none;
    box-shadow: 
        10vw 20vh 3px #fff, 25vw 45vh 2px #00FF66, 80vw 15vh 3px #fff,
        45vw 70vh 4px #fff, 90vw 85vh 2px #00FF66, 15vw 80vh 3px #fff,
        65vw 35vh 2px #fff, 75vw 60vh 3px #fff, 35vw 10vh 2px #00FF66,
        5vw 50vh 3px #fff, 55vw 20vh 4px #fff, 70vw 90vh 1px #fff,
        85vw 50vh 3px #00FF66, 20vw 30vh 2px #fff, 60vw 75vh 4px #fff;
    animation: twinStars 6s ease-in-out infinite alternate;
}

@keyframes twinStars {
    0% { transform: translateY(0px) scale(0.9); opacity: 0.4; }
    100% { transform: translateY(-30px) scale(1.1); opacity: 0.9; }
}

/* App UI Layout Formatting */
h1, h2, h3, h4 { 
    color: #00FF66 !important; 
    font-family: 'Arial', sans-serif; 
    text-shadow: 0px 0px 10px rgba(0, 255, 102, 0.4); 
}
.stSelectbox label, .stSlider label, .stTextInput label, div[data-testid="stMarkdownContainer"] p { 
    color: white !important; 
    font-weight: bold; 
}
div[data-testid="stMetricValue"] { 
    color: #00FF66 !important; 
    font-weight: bold; 
}
.card { 
    background: rgba(255, 255, 255, 0.04); padding: 1.5rem; border-radius: 12px; 
    border: 1px solid rgba(0, 255, 102, 0.15); margin-bottom: 1rem; backdrop-filter: blur(12px); color: white; 
}
.card:hover { transform: translateY(-5px); border-color: #00FF66; box-shadow: 0px 5px 20px rgba(0, 255, 102, 0.25); }
.kpi-box { background: linear-gradient(135deg, rgba(0, 255, 102, 0.12), rgba(0, 204, 82, 0.05)); border-radius: 12px; padding: 1rem; text-align: center; border: 1px solid #00FF66; color: white; }
.winner-banner { background: linear-gradient(90deg, #00FF66, #00CC52); color: black !important; padding: 15px; border-radius: 12px; text-align: center; font-weight: bold; font-size: 24px; margin-bottom: 25px; box-shadow: 0px 4px 15px rgba(0, 255, 102, 0.4); }
</style>
""", unsafe_allow_html=True)

st.title("⚡ IPL Pro Analytics Engine")

# 3. Master Completed Database Matrix (Part 1 - Teams RCB & CSK and others team in ipl)
teams = {
    "RCB": {
        "Virat Kohli": {"Role": "Opening Batsman", "Matches": 260, "Runs": 8500, "Highest Record": "973 Runs in One Season", "Image": "default.jpg"},
        "Rajat Patidar": {"Role": "Batsman", "Matches": 24, "Runs": 790, "Highest Record": "Fastest Playoff Century by Uncapped", "Image": "default.jpg"},
        "Yash Dayal": {"Role": "Bowler", "Matches": 28, "Wickets": 25, "Highest Record": "Phenomenal 20th Over Defence", "Image": "default.jpg"},
        "Glenn Maxwell": {"Role": "All-Rounder", "Matches": 130, "Runs": 2800, "Wickets": 37, "Highest Record": "Most Switch-Hit Sixes", "Image": "default.jpg"},
        "Mohammed Siraj": {"Role": "Bowler", "Matches": 110, "Wickets": 110, "Highest Record": "Powerplay Specialist", "Image": "default.jpg"},
        "Faf du Plessis": {"Role": "Opening Batsman", "Matches": 150, "Runs": 4700, "Highest Record": "Consistent Overseas Batter", "Image": "default.jpg"},
        "Cameron Green": {"Role": "All-Rounder", "Matches": 29, "Runs": 700, "Wickets": 16, "Highest Record": "Fastest Hundred at Wankhede", "Image": "default.jpg"},
        "Josh Hazlewood": {"Role": "Bowler", "Matches": 40, "Wickets": 55, "Highest Record": "World-Class Fast Bowler", "Image": "default.jpg"},
        "Anuj Rawat": {"Role": "Wicketkeeper", "Matches": 24, "Runs": 320, "Highest Record": "Brilliant Dynamic Catching Rate", "Image": "default.jpg"},
        "Mahipal Lomror": {"Role": "All-Rounder", "Matches": 40, "Runs": 540, "Highest Record": "Highest Strike Rate as Impact Player", "Image": "default.jpg"}
    },

"CSK": {
        "Ruturaj Gaikwad": {"Role": "Opening Batsman", "Matches": 66, "Runs": 2380, "Highest Record": "Orange Cap Winner", "Image": "default.jpg"},
        "MS Dhoni": {"Role": "Wicketkeeper-Batsman", "Matches": 264, "Runs": 5343, "Highest Record": "Most Keeper Dismissals (190)", "Image": "default.jpg"},
        "Ravindra Jadeja": {"Role": "All-Rounder", "Matches": 240, "Runs": 2958, "Wickets": 160, "Highest Record": "Most Catch for CSK Franchise", "Image": "default.jpg"},
        "Shivam Dube": {"Role": "All-Rounder", "Matches": 65, "Runs": 1520, "Highest Record": "Highest Spin Strike Rate", "Image": "default.jpg"},
        "Matheesha Pathirana": {"Role": "Bowler", "Matches": 20, "Wickets": 34, "Highest Record": "Best Death Overs Economy", "Image": "default.jpg"},
        "Ajinkya Rahane": {"Role": "Opening Batsman", "Matches": 195, "Runs": 4900, "Highest Record": "Experienced Top Order Batter", "Image": "default.jpg"},
        "Deepak Chahar": {"Role": "Bowler", "Matches": 90, "Wickets": 85, "Highest Record": "Swing Bowling Expert", "Image": "default.jpg"},
        "Tushar Deshpande": {"Role": "Bowler", "Matches": 36, "Wickets": 42, "Highest Record": "Highest Wickets in 2023 for CSK", "Image": "default.jpg"},
        "Mitchell Santner": {"Role": "All-Rounder", "Matches": 18, "Wickets": 15, "Highest Record": "Lowest Economy for Overseas Spinner", "Image": "default.jpg"},
        "Rachin Ravindra": {"Role": "All-Rounder", "Matches": 20, "Runs": 450, "Highest Record": "Dynamic Opening Batter", "Image": "default.jpg"}
    },
"MI": {
        "Rohit Sharma": {"Role": "Opening Batsman", "Matches": 270, "Runs": 7000, "Highest Record": "5 IPL Titles as Captain", "Image": "default.jpg"},
        "Jasprit Bumrah": {"Role": "Bowler", "Matches": 133, "Wickets": 165, "Highest Record": "Best Playoff Economy", "Image": "default.jpg"},
        "Suryakumar Yadav": {"Role": "Batsman", "Matches": 150, "Runs": 3500, "Highest Record": "Most 360-degree Boundaries", "Image": "default.jpg"},
        "Hardik Pandya": {"Role": "All-Rounder", "Matches": 137, "Runs": 2500, "Wickets": 64, "Highest Record": "Multi-title Winning All-Rounder", "Image": "default.jpg"},
        "Tilak Varma": {"Role": "Batsman", "Matches": 38, "Runs": 1200, "Highest Record": "Consistent Middle-Order Average", "Image": "default.jpg"},
        "Ishan Kishan": {"Role": "Wicketkeeper-Batsman", "Matches": 115, "Runs": 2800, "Highest Record": "Aggressive Opening Batter", "Image": "default.jpg"},
        "Tim David": {"Role": "Finisher", "Matches": 45, "Runs": 900, "Highest Record": "Strike Rate Above 170", "Image": "default.jpg"},
        "Piyush Chawla": {"Role": "Bowler", "Matches": 192, "Wickets": 192, "Highest Record": "Top 3 Highest Wicket Taker", "Image": "default.jpg"},
        "Gerald Coetzee": {"Role": "Bowler", "Matches": 15, "Wickets": 18, "Highest Record": "Highest Pace Clocked for MI", "Image": "default.jpg"},
        "Naman Dhir": {"Role": "All-Rounder", "Matches": 20, "Runs": 300, "Highest Record": "Emerging Talent", "Image": "default.jpg"}
    },
"KKR": {
        "Shreyas Iyer": {"Role": "Batsman", "Matches": 116, "Runs": 3127, "Highest Record": "Led KKR to 2024 Title", "Image": "default.jpg"},
        "Rinku Singh": {"Role": "Finisher", "Matches": 46, "Runs": 893, "Highest Record": "5 Sixes in 5 Balls", "Image": "default.jpg"},
        "Sunil Narine": {"Role": "All-Rounder", "Matches": 174, "Runs": 1500, "Wickets": 180, "Highest Record": "Most MVP Awards in IPL History", "Image": "default.jpg"},
        "Andre Russell": {"Role": "All-Rounder", "Matches": 120, "Runs": 2400, "Wickets": 115, "Highest Record": "Highest Career Strike Rate (174+)", "Image": "default.jpg"},
        "Varun Chakaravarthy": {"Role": "Bowler", "Matches": 70, "Wickets": 86, "Highest Record": "Best Mystery Spinner Stats", "Image": "default.jpg"},
        "Venkatesh Iyer": {"Role": "All-Rounder", "Matches": 50, "Runs": 1300, "Highest Record": "Top Scorer in 2024 Finals", "Image": "default.jpg"},
        "Harshit Rana": {"Role": "Bowler", "Matches": 15, "Wickets": 22, "Highest Record": "Best Slower-Ball Variation", "Image": "default.jpg"},
        "Ramandeep Singh": {"Role": "Finisher", "Matches": 20, "Runs": 250, "Highest Record": "Exceptional Outfield Catching Rate", "Image": "default.jpg"},
        "Mitchell Starc": {"Role": "Bowler", "Matches": 45, "Wickets": 55, "Highest Record": "World-Class Left Arm Fast Bowler", "Image": "default.jpg"},
        "Phil Salt": {"Role": "Wicketkeeper-Batsman", "Matches": 30, "Runs": 900, "Highest Record": "Explosive Powerplay Batter", "Image": "default.jpg"}
    },
"SRH": {
        "Pat Cummins": {"Role": "Bowler-Captain", "Matches": 58, "Wickets": 62, "Highest Record": "Led SRH to 2024 Final", "Image": "default.jpg"},
        "Abhishek Sharma": {"Role": "Opening Batsman", "Matches": 63, "Runs": 1370, "Highest Record": "Most Sixes by an Indian in a Season", "Image": "default.jpg"},
        "Travis Head": {"Role": "Opening Batsman", "Matches": 30, "Runs": 900, "Highest Record": "Fastest Century for SRH", "Image": "default.jpg"},
        "Heinrich Klaasen": {"Role": "Wicketkeeper-Batsman", "Matches": 35, "Runs": 1100, "Highest Record": "Highest Strike Rate Against Spin", "Image": "default.jpg"},
        "Nitish Kumar Reddy": {"Role": "All-Rounder", "Matches": 15, "Runs": 303, "Highest Record": "Emerging Player of the Year 2024", "Image": "default.jpg"},
        "T Natarajan": {"Role": "Bowler", "Matches": 70, "Wickets": 75, "Highest Record": "Yorker Specialist", "Image": "default.jpg"},
        "Bhuvneshwar Kumar": {"Role": "Bowler", "Matches": 186, "Wickets": 193, "Highest Record": "2× Purple Cap Winner", "Image": "default.jpg"},
        "Shahbaz Ahmed": {"Role": "All-Rounder", "Matches": 50, "Runs": 450, "Wickets": 20, "Highest Record": "Crucial Partnership Breaker", "Image": "default.jpg"},
        "Mohammed Shami": {"Role": "Bowler", "Matches": 115, "Wickets": 135, "Highest Record": "Powerplay Wicket Taker", "Image": "default.jpg"},
        "Washington Sundar": {"Role": "All-Rounder", "Matches": 70, "Runs": 450, "Wickets": 40, "Highest Record": "Economical Off Spinner", "Image": "default.jpg"}
    },
"RR": {
        "Sanju Samson": {"Role": "Wicketkeeper-Batsman", "Matches": 180, "Runs": 4800, "Highest Record": "RR Captain & Leader", "Image": "default.jpg"},
        "Yashasvi Jaiswal": {"Role": "Opening Batsman", "Matches": 70, "Runs": 2200, "Highest Record": "Young Indian Star", "Image": "default.jpg"},
        "Riyan Parag": {"Role": "All-Rounder", "Matches": 85, "Runs": 1500, "Wickets": 10, "Highest Record": "Most Improved Player", "Image": "default.jpg"},
        "Dhruv Jurel": {"Role": "Wicketkeeper-Batsman", "Matches": 35, "Runs": 500, "Highest Record": "Outstanding Striker", "Image": "default.jpg"},
        "Shimron Hetmyer": {"Role": "Finisher", "Matches": 85, "Runs": 1500, "Highest Record": "Explosive Finisher", "Image": "default.jpg"},
        "Yuzvendra Chahal": {"Role": "Bowler", "Matches": 160, "Wickets": 205, "Highest Record": "All-Time Highest Wicket Taker in IPL", "Image": "default.jpg"},
        "Ravichandran Ashwin": {"Role": "All-Rounder", "Matches": 220, "Runs": 850, "Wickets": 190, "Highest Record": "Legendary Off Spinner", "Image": "default.jpg"},
        "Trent Boult": {"Role": "Bowler", "Matches": 115, "Wickets": 140, "Highest Record": "Powerplay Wicket Specialist", "Image": "default.jpg"},
        "Adam Zampa": {"Role": "Bowler", "Matches": 25, "Wickets": 30, "Highest Record": "World-Class Leg Spinner", "Image": "default.jpg"},
        "Prasidh Krishna": {"Role": "Bowler", "Matches": 60, "Wickets": 65, "Highest Record": "Tall Fast Bowler", "Image": "default.jpg"}
    },
 "GT": {
        "Shubman Gill": {"Role": "Opening Batsman", "Matches": 120, "Runs": 3800, "Highest Record": "Orange Cap Winner", "Image": "default.jpg"},
        "Rashid Khan": {"Role": "Bowler", "Matches": 130, "Wickets": 165, "Highest Record": "Fastest to 100 IPL Wickets", "Image": "default.jpg"},
        "Sai Sudharsan": {"Role": "Opening Batsman", "Matches": 40, "Runs": 1500, "Highest Record": "Emerging Indian Batter", "Image": "default.jpg"},
        "Rahul Tewatia": {"Role": "All-Rounder", "Matches": 100, "Runs": 1100, "Wickets": 35, "Highest Record": "Famous Last Over Finisher", "Image": "default.jpg"},
        "David Miller": {"Role": "Finisher", "Matches": 130, "Runs": 2900, "Highest Record": "Killer Miller Unbeaten Records", "Image": "default.jpg"},
        "Mohit Sharma": {"Role": "Bowler", "Matches": 120, "Wickets": 135, "Highest Record": "Death Overs Specialist", "Image": "default.jpg"},
        "Noor Ahmad": {"Role": "Bowler", "Matches": 25, "Wickets": 35, "Highest Record": "Mystery Left-Arm Spinner", "Image": "default.jpg"},
        "Jos Buttler": {"Role": "Wicketkeeper-Batsman", "Matches": 115, "Runs": 3900, "Highest Record": "Orange Cap Winner", "Image": "default.jpg"},
        "Sherfane Rutherford": {"Role": "Finisher", "Matches": 35, "Runs": 500, "Highest Record": "Power Hitter", "Image": "default.jpg"},
        "Devon Conway": {"Role": "Opening Batsman", "Matches": 35, "Runs": 1000, "Highest Record": "Consistent Run Scorer", "Image": "default.jpg"}
    },"LSG": {
        "KL Rahul": {"Role": "Wicketkeeper-Batsman", "Matches": 145, "Runs": 5000, "Highest Record": "Orange Cap Winner", "Image": "default.jpg"},
        "Nicholas Pooran": {"Role": "Finisher", "Matches": 76, "Runs": 1769, "Highest Record": "Highest Death Strike Rate", "Image": "default.jpg"},
        "Ravi Bishnoi": {"Role": "Bowler", "Matches": 66, "Wickets": 63, "Highest Record": "Fastest Googlies in Business", "Image": "default.jpg"},
        "Krunal Pandya": {"Role": "All-Rounder", "Matches": 145, "Runs": 1800, "Wickets": 90, "Highest Record": "Consistent All-Round Performer", "Image": "default.jpg"},
        "Quinton de Kock": {"Role": "Wicketkeeper-Batsman", "Matches": 115, "Runs": 3300, "Highest Record": "Explosive Left-Hand Opener", "Image": "default.jpg"},
        "Karun Nair": {"Role": "Batsman", "Matches": 85, "Runs": 1600, "Highest Record": "Triple Century in Test Cricket", "Image": "default.jpg"},
        "Nitish Rana": {"Role": "Batsman", "Matches": 115, "Runs": 2800, "Highest Record": "Reliable Middle Order Batter", "Image": "default.jpg"},
        "Mayank Yadav": {"Role": "Bowler", "Matches": 4, "Wickets": 7, "Highest Record": "Back-to-Back 155+ kmph Deliveries", "Image": "default.jpg"},
        "Mohsin Khan": {"Role": "Bowler", "Matches": 24, "Wickets": 31, "Highest Record": "Defended 11 Runs in Last Over", "Image": "default.jpg"},
        "Naveen-ul-Haq": {"Role": "Bowler", "Matches": 22, "Wickets": 25, "Highest Record": "Brilliant Back-of-the-hand Slower balls", "Image": "default.jpg"}
    },
"DC": {
        "Rishabh Pant": {"Role": "Keeper-Batsman", "Matches": 111, "Runs": 3284, "Highest Record": "Highest Indian Score (128*)", "Image": "default.jpg"},
        "Axar Patel": {"Role": "All-Rounder", "Matches": 165, "Runs": 1800, "Wickets": 130, "Highest Record": "Reliable Spin All-Rounder", "Image": "default.jpg"},
        "Kuldeep Yadav": {"Role": "Bowler", "Matches": 95, "Wickets": 100, "Highest Record": "Chinaman Spin Specialist", "Image": "default.jpg"},
        "Tristan Stubbs": {"Role": "Batsman", "Matches": 30, "Runs": 700, "Highest Record": "Explosive Finisher", "Image": "default.jpg"},
        "Khaleel Ahmed": {"Role": "Bowler", "Matches": 70, "Wickets": 80, "Highest Record": "Left-Arm Pace Specialist", "Image": "default.jpg"},
        "Anrich Nortje": {"Role": "Bowler", "Matches": 50, "Wickets": 65, "Highest Record": "150+ km/h Fast Bowler", "Image": "default.jpg"},
        "Abishek Porel": {"Role": "Wicketkeeper-Batsman", "Matches": 20, "Runs": 350, "Highest Record": "Impactful Quickfire Runs at Top", "Image": "default.jpg"},
        "Jake Fraser-McGurk": {"Role": "Opening Batsman", "Matches": 9, "Runs": 330, "Highest Record": "Highest Powerplay Strike Rate (230+)", "Image": "default.jpg"},
        "Mukesh Kumar": {"Role": "Bowler", "Matches": 24, "Wickets": 26, "Highest Record": "Best Block-hole Bowling Control", "Image": "default.jpg"},
        "Prithvi Shaw": {"Role": "Opening Batsman", "Matches": 79, "Runs": 1800, "Highest Record": "6 Fours in One Over", "Image": "default.jpg"}
    },
"PBKS": {
        "Shashank Singh": {"Role": "All-Rounder", "Matches": 24, "Runs": 450, "Highest Record": "Highest Strike Rate in Death", "Image": "default.jpg"},
        "Arshdeep Singh": {"Role": "Bowler", "Matches": 65, "Wickets": 76, "Highest Record": "Leading T20 Death Bowler", "Image": "default.jpg"},
        "Jitesh Sharma": {"Role": "Wicketkeeper-Batsman", "Matches": 45, "Runs": 850, "Highest Record": "Aggressive Middle-Order Finisher", "Image": "default.jpg"},
        "Liam Livingstone": {"Role": "All-Rounder", "Matches": 45, "Runs": 950, "Wickets": 12, "Highest Record": "Power-Hitting All-Rounder", "Image": "default.jpg"},
        "Harshal Patel": {"Role": "Bowler", "Matches": 110, "Wickets": 150, "Highest Record": "Purple Cap Winner", "Image": "default.jpg"},
        "Prabhsimran Singh": {"Role": "Wicketkeeper-Batsman", "Matches": 34, "Runs": 750, "Highest Record": "Aggressive Opening Century", "Image": "default.jpg"},
        "Sam Curran": {"Role": "All-Rounder", "Matches": 59, "Runs": 900, "Wickets": 55, "Highest Record": "Highest Paid All-Rounder Captain", "Image": "default.jpg"},
        "Kagiso Rabada": {"Role": "Bowler", "Matches": 80, "Wickets": 117, "Highest Record": "Fastest to 100 IPL Wickets", "Image": "default.jpg"},
        "David Warner": {"Role": "Opening Batsman", "Matches": 184, "Runs": 6560, "Highest Record": "Most Fifties in IPL History", "Image": "default.jpg"},
        "Ashutosh Sharma": {"Role": "Finisher", "Matches": 11, "Runs": 190, "Highest Record": "Highest Strike Rate in Debut Season", "Image": "default.jpg"}
    }
}
# 4. Multi-Page Navigation Layout Settings
st.sidebar.title("🎵 Navigation")
page = st.sidebar.radio("Go to:", ["Teams View", "Compare Players"])
st.sidebar.markdown("---")

# ================= PAGE A: TEAMS VIEW LAYOUT =================
if page == "Teams View":
    st.markdown("<div class='winner-banner'>🏆 10 Franchises Live Performance Matrix</div>", unsafe_allow_html=True)
    selected_team = st.sidebar.selectbox("Choose Franchise Team:", list(teams.keys()))
    
    st.sidebar.markdown("---")
    search_query = st.sidebar.text_input("🔍 Search Player by Name:", "")
    min_runs = st.sidebar.slider("⚡ Min Runs Filter:", 0, 9000, 0, step=100)
    
    if selected_team:
        player_dict = teams[selected_team]
        total_matches = sum(p["Matches"] for p in player_dict.values())
        total_runs = sum(p.get("Runs", 0) for p in player_dict.values())
        total_wickets = sum(p.get("Wickets", 0) for p in player_dict.values())
        
        st.subheader(f"✨ {selected_team} Squad Matrix Summary (10 Stars Active)")
        kpi1, kpi2, kpi3 = st.columns(3)
        with kpi1: st.markdown(f"<div class='kpi-box'>📋 <b>Squad Total Matches</b><h3>{total_matches}</h3></div>", unsafe_allow_html=True)
        with kpi2: st.markdown(f"<div class='kpi-box'>🏏 <b>Squad Cumulative Runs</b><h3>{total_runs}</h3></div>", unsafe_allow_html=True)
        with kpi3: st.markdown(f"<div class='kpi-box'>🎯 <b>Squad Cumulative Wickets</b><h3>{total_wickets}</h3></div>", unsafe_allow_html=True)
        
        st.markdown("<br>---<br>", unsafe_allow_html=True)
        
        cols = st.columns(2)
        grid_idx = 0
        for p_name, details in player_dict.items():
            if search_query and search_query.lower() not in p_name.lower(): continue
            if min_runs > 0 and details.get("Runs", 0) < min_runs: continue
            
            with cols[grid_idx % 2]:
                st.markdown(f"<div class='card'><h3 style='margin:0;'>{p_name}</h3><p style='margin:5px 0 0 0; color:#00FF66;'><b>Role:</b> {details['Role']}</p></div>", unsafe_allow_html=True)
                st.image("https://flaticon.com", width=85)
                
                sub1, sub2 = st.columns(2)
                sub1.metric("Matches Played", details["Matches"])
                if "Wickets" in details and "Runs" in details: sub2.metric("Runs / Wickets", f"{details['Runs']}R / {details['Wickets']}W")
                elif "Wickets" in details: sub2.metric("Total Wickets", details["Wickets"])
                else: sub2.metric("Total Runs", details["Runs"])
                st.warning(f"🏅 {details['Highest Record']}")
                st.markdown("<br>", unsafe_allow_html=True)
            grid_idx += 1

# ================= PAGE B: COMPARE PLAYERS ENGINE =================
else:
    st.markdown("<div class='winner-banner'>⚔️ Player Comparison Analytics Hub</div>", unsafe_allow_html=True)
    
    all_players_flat = {}
    for t_name, squad in teams.items():
        for p_name, data in squad.items():
            all_players_flat[p_name] = {"team": t_name, **data}
            
    col_sel1, col_col2 = st.columns(2)
    with col_sel1: player1 = st.selectbox("Select Player 1:", list(all_players_flat.keys()), index=0)
    with col_col2: player2 = st.selectbox("Select Player 2:", list(all_players_flat.keys()), index=4)
    
    if player1 and player2:
        p1_data = all_players_flat[player1]
        p2_data = all_players_flat[player2]
        
        comp_col1, comp_col2 = st.columns(2)
        with comp_col1:
            st.markdown(f"<div class='card'><h2>{player1}</h2><h4>Franchise: {p1_data['team']}</h4><p><b>Role:</b> {p1_data['Role']}</p></div>", unsafe_allow_html=True)
            st.metric("Matches Career", p1_data["Matches"])
            if "Runs" in p1_data: st.metric("Total Runs", p1_data["Runs"])
            if "Wickets" in p1_data: st.metric("Total Wickets", p1_data["Wickets"])
            st.info(f"🏅 Record: {p1_data['Highest Record']}")
            
        with comp_col2:
            st.markdown(f"<div class='card'><h2>{player2}</h2><h4>Franchise: {p2_data['team']}</h4><p><b>Role:</b> {p2_data['Role']}</p></div>", unsafe_allow_html=True)
            st.metric("Matches Career", p2_data["Matches"])
            if "Runs" in p2_data: st.metric("Total Runs", p2_data["Runs"])
            if "Wickets" in p2_data: st.metric("Total Wickets", p2_data["Wickets"])
            st.info(f"🏅 Record: {p2_data['Highest Record']}")
            # ===========================
# PROJECT STATISTICS
# ===========================

st.markdown("---")
st.header("📊 IPL Project Statistics")

total_teams = len(teams)

total_players = sum(len(team) for team in teams.values())

total_matches = sum(
    player["Matches"]
    for team in teams.values()
    for player in team.values()
)

total_runs = sum(
    player.get("Runs", 0)
    for team in teams.values()
    for player in team.values()
)

total_wickets = sum(
    player.get("Wickets", 0)
    for team in teams.values()
    for player in team.values()
)

c1, c2, c3, c4, c5 = st.columns(5)

with c1:
    st.metric("🏏 Teams", total_teams)

with c2:
    st.metric("👥 Players", total_players)

with c3:
    st.metric("🎮 Matches", total_matches)

with c4:
    st.metric("🏏 Runs", total_runs)

with c5:
    st.metric("🎯 Wickets", total_wickets)

st.markdown("---")

# ===========================
# CELEBRATION
# ===========================

st.subheader("🎉 Celebrate IPL")

if st.button("🏆 Celebrate"):
    st.balloons()
    st.success("Congratulations! Welcome to IPL Pro Analytics Hub 🎊")

st.markdown("---")


st.markdown(
    """
    <div style='text-align:center;
                padding:20px;
                border-top:1px solid #00FF66;
                color:white;'>

    <h3 style='color:#00FF66;'>🏏 IPL Pro Analytics Hub</h3>

    <p>Developed By</p>

    <b>
    Utkarsh 
    </b>

    <br><br>

    <p>Built using ❤️ Python • Streamlit</p>

    <p>© 2026 All Rights Reserved</p>

    </div>
    """,
    unsafe_allow_html=True,
)
# ======================================================
# 🏆 IPL HALL OF FAME
# ======================================================

all_players = []

for team_name, squad in teams.items():
    for player_name, details in squad.items():
        all_players.append({
            "Team": team_name,
            "Player": player_name,
            "Runs": details.get("Runs", 0),
            "Wickets": details.get("Wickets", 0),
            "Matches": details.get("Matches", 0),
            "Role": details.get("Role", "")
        })

highest_run = max(all_players, key=lambda x: x["Runs"])
highest_wicket = max(all_players, key=lambda x: x["Wickets"])
most_experience = max(all_players, key=lambda x: x["Matches"])

st.markdown("---")
st.header("🏆 IPL Hall of Fame")

c1, c2, c3 = st.columns(3)

with c1:
    st.success("🏏 Highest Run Scorer")
    st.metric(highest_run["Player"], highest_run["Runs"])
    st.caption(highest_run["Team"])

with c2:
    st.success("🎯 Highest Wicket Taker")
    st.metric(highest_wicket["Player"], highest_wicket["Wickets"])
    st.caption(highest_wicket["Team"])

with c3:
    st.success("👑 Most Experienced")
    st.metric(most_experience["Player"], most_experience["Matches"])
    st.caption(most_experience["Team"])


# ======================================================
# ⭐ RANDOM PLAYER SPOTLIGHT
# ======================================================

import random

spotlight = random.choice(all_players)

st.markdown("---")
st.subheader("⭐ Player Spotlight")

st.info(
    f"""
### {spotlight['Player']}

🏏 Team : {spotlight['Team']}

🎮 Matches : {spotlight['Matches']}

🏃 Runs : {spotlight['Runs']}

🎯 Wickets : {spotlight['Wickets']}

👤 Role : {spotlight['Role']}
"""
)


# ======================================================
# 💡 IPL FUN FACTS
# ======================================================

facts = [
    "🏏 Virat Kohli is among the highest run scorers in IPL history.",
    "🎯 Yuzvendra Chahal has been one of the leading wicket takers in IPL.",
    "🏆 Mumbai Indians and Chennai Super Kings are among the most successful IPL franchises.",
    "🔥 MS Dhoni is famous for finishing matches under pressure.",
    "💥 Chris Gayle holds the record for the highest individual IPL score (175*).",
    "⚡ AB de Villiers is known as Mr. 360 because of his innovative shots.",
    "🚀 Jasprit Bumrah is one of the best death-over bowlers in T20 cricket."
]

st.markdown("---")
st.subheader("💡 IPL Fun Fact")

st.warning(random.choice(facts))


# ======================================================
# 🎉 CELEBRATE BUTTON
# ======================================================

st.markdown("---")

if st.button("🎉 Celebrate IPL"):
    st.balloons()
    st.success("🏆 Welcome to IPL Pro Analytics Hub")


# ======================================================
# ❤️ FOOTER
# ======================================================

st.markdown("---")

st.markdown(
"""
<div style='text-align:center;padding:20px;'>

<h2 style='color:#00FF66;'>🏏 IPL Pro Analytics Hub</h2>

<h4>Developed By</h4>

<b>Utkarsh Srivastav brijendra singh manish Aman</b>

<br><br>

Made with ❤️ using Python & Streamlit

<br><br>

© 2026 IPL Analytics Project

</div>
""",
unsafe_allow_html=True
)
# ==========================================================
# 🏆 EXTRA ANALYTICS SECTION (Paste at the END of your code)
# ==========================================================

import random

st.markdown("---")
st.header("🏆 Advanced IPL Analytics")

# ---------- Collect All Players ----------
all_players = []

for team, squad in teams.items():
    for player, info in squad.items():
        all_players.append({
            "Player": player,
            "Team": team,
            "Runs": info.get("Runs", 0),
            "Wickets": info.get("Wickets", 0),
            "Matches": info.get("Matches", 0),
            "Role": info.get("Role", "")
        })

# ---------- TOP 5 RUN SCORERS ----------
st.subheader("🏏 Top 5 Run Scorers")

top_runs = sorted(all_players, key=lambda x: x["Runs"], reverse=True)[:5]

for i, p in enumerate(top_runs, 1):
    st.write(f"{i}. **{p['Player']}** ({p['Team']}) - {p['Runs']} Runs")

st.markdown("---")

# ---------- TOP 5 WICKET TAKERS ----------
st.subheader("🎯 Top 5 Wicket Takers")

top_wickets = sorted(all_players, key=lambda x: x["Wickets"], reverse=True)[:5]

for i, p in enumerate(top_wickets, 1):
    st.write(f"{i}. **{p['Player']}** ({p['Team']}) - {p['Wickets']} Wickets")

st.markdown("---")

# ---------- TEAM RANKINGS ----------
st.subheader("🥇 Team Rankings")

team_scores = []

for team, squad in teams.items():

    runs = sum(x.get("Runs", 0) for x in squad.values())
    wickets = sum(x.get("Wickets", 0) for x in squad.values())

    score = runs + wickets * 20

    team_scores.append((team, score))

team_scores = sorted(team_scores, key=lambda x: x[1], reverse=True)

for rank, (team, score) in enumerate(team_scores, 1):
    st.write(f"{rank}. 🏏 {team} — {score} Points")

st.markdown("---")

# ---------- RANDOM PLAYER ----------
st.subheader("🎲 Random Player Generator")

if st.button("🎲 Pick Random Player"):
    player = random.choice(all_players)

    st.success(f"⭐ {player['Player']}")

    st.write(f"**Team :** {player['Team']}")
    st.write(f"**Role :** {player['Role']}")
    st.write(f"**Matches :** {player['Matches']}")
    st.write(f"**Runs :** {player['Runs']}")
    st.write(f"**Wickets :** {player['Wickets']}")

st.markdown("---")

# ---------- IPL QUIZ ----------
st.subheader("🧠 IPL Quiz")

answer = st.radio(
    "Who is known for scoring 973 runs in one IPL season?",
    [
        "MS Dhoni",
        "Virat Kohli",
        "Rohit Sharma",
        "KL Rahul"
    ]
)

if st.button("Submit Answer"):

    if answer == "Virat Kohli":
        st.success("✅ Correct Answer!")
        st.balloons()
    else:
        st.error("❌ Wrong Answer. Correct Answer: Virat Kohli")

st.markdown("---")
# ======================================================
# QUIZ 2
# ======================================================

st.markdown("---")
st.subheader("🧠 IPL Quiz 2")

answer2 = st.radio(
    "Which player is known as 'Mr. 360' in IPL?",
    [
        "AB de Villiers",
        "MS Dhoni",
        "Rohit Sharma",
        "Suresh Raina"
    ],
    key="quiz2"
)

if st.button("Submit Quiz 2"):

    if answer2 == "AB de Villiers":
        st.success("✅ Correct Answer!")
        st.balloons()
    else:
        st.error("❌ Wrong Answer. Correct Answer: AB de Villiers")
        # ======================================================
# QUIZ 3
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