import streamlit as st
import pandas as pd
import numpy as np
from utils.data_loader import load_player_mapping, load_bayesian_data, load_shots_data
from utils.plotly_theme import COLORS
import plotly.io as pio
pio.templates.default = 'xg_dark'

st.set_page_config(page_title="Player Profiles", page_icon="👤", layout="wide")


st.markdown("""
<style>
[data-testid="stHeaderActionElements"] {
    display: none !important;
}
</style>
""", unsafe_allow_html=True)

st.title("👤 Player Profiles")
st.markdown("Explore individual finishing fingerprints and specialization patterns")

# Load data
player_mapping = load_player_mapping()
bayesian_data = load_bayesian_data()
shots_data = load_shots_data()

player_names = sorted(player_mapping['player_name'].tolist())

st.markdown("---")

# Player selection
st.subheader("Select Player")

player_options = ["-- Select a player --"] + player_names

selected_player = st.selectbox(
    "Choose a player to analyze:",
    options=player_options,
    index=0
)

if selected_player == "-- Select a player --":
    st.info("Please select a player from the dropdown above to view their finishing profile")
    st.stop()
with st.spinner(f"Loading profile for {selected_player}..."):
    # Get player data
    player_id = player_mapping[player_mapping['player_name'] == selected_player]['player_id'].values[0]

    # Get player data
    player_row = player_mapping[player_mapping['player_name'] == selected_player].iloc[0]
    player_id = player_row['player_id']
    player_coeffs = np.array(bayesian_data['players'][selected_player]['coeffs'])
    player_uncertainty = np.array(bayesian_data['players'][selected_player]['uncertainty'])
    global_betas = np.array(bayesian_data['model_params']['global_betas'])

    # FM17 ratings
    fm_finishing = player_row['raw_finishing']
    fm_longshots = player_row['raw_longshots']

    st.markdown("---")

# Basic info
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("FM17 Finishing", fm_finishing)
with col2:
    st.metric("FM17 Long Shots", fm_longshots)
with col3:
    player_shots = shots_data[shots_data['player_id'] == player_id]
    st.metric("Total Shots", len(player_shots))
with col4:
    goals = player_shots['is_goal'].sum()
    st.metric("Goals Scored", int(goals))

st.markdown("---")

# Radar chart - Finishing Fingerprint
st.subheader("Finishing Fingerprint")
st.caption("Player coefficients compared to global average (all 17 features)")

import plotly.graph_objects as go

# Feature names for radar
feature_names = [
    "Distance", "GK Distance", "Angle",
    "Left Foot", "Headers", "Right Foot",
    "Diving Headers", "Half Volley", "Lob",
    "Normal Tech", "Overhead", "Volley",
    "First Time", "1v1", "Pressure",
    "Penalty Area", "Defenders"
]

# All features
player_values = player_coeffs.tolist()
global_values = global_betas.tolist()

# Create radar chart
fig_radar = go.Figure()

# Global average
fig_radar.add_trace(go.Scatterpolar(
    r=global_values,
    theta=feature_names,
    fill='toself',
    fillcolor='rgba(139, 92, 246, 0.2)',  # bayesian_purple
    line=dict(color=COLORS['bayesian_purple'], width=2),
    name='Global Average'
))

# Player
fig_radar.add_trace(go.Scatterpolar(
    r=player_values,
    theta=feature_names,
    fill='toself',
    fillcolor='rgba(59, 130, 246, 0.3)',  # xg_blue
    line=dict(color=COLORS['xg_blue'], width=3),
    name=selected_player
))

fig_radar.update_layout(
    polar=dict(
        bgcolor='#0A0F1E',
        radialaxis=dict(
            visible=True,
            gridcolor='#1E2D45',
            color='#E8EDF5'
        ),
        angularaxis=dict(
            gridcolor='#1E2D45',
            color='#E8EDF5'
        )
    ),
    showlegend=True,
    legend=dict(
        bgcolor='#0A0F1E',
        font=dict(color='#E8EDF5')
    ),
    height=600,
    paper_bgcolor='#0A0F1E',
    font=dict(color='#E8EDF5')
)

st.plotly_chart(fig_radar, use_container_width=True)

with st.expander("ℹ️ How to read this radar chart"):
    st.markdown("""
    - **Cyan area** = This player's coefficients
    - **Orange area** = Global average (population)
    - **Larger cyan area** = Player excels in those situations
    - **Smaller cyan area** = Player struggles relative to average
    
    All 17 model features are shown. Values represent contribution to the logit (pre-sigmoid).
    """)
    st.markdown("---")

# Shot history
st.subheader("Shot History")
st.caption(f"All {len(player_shots)} shots from the 2015-16 season")

# Prepare shot data for display
if len(player_shots) > 0:
    display_shots = player_shots[[
        'shot_distance', 'shot_angle', 'shot_body_part', 'shot_technique',
        'shot_first_time', 'shot_one_on_one', 'under_pressure',
        'within_penalty_area', 'num_defenders_in_triangle', 'is_goal'
    ]].copy()
    
    # Rename columns for readability
    display_shots.columns = [
        'Distance (m)', 'Angle (rad)', 'Body Part', 'Technique',
        'First Time', '1v1', 'Pressure', 'In Box', 'Defenders', 'Goal'
    ]
    
    # Format booleans
    display_shots['First Time'] = display_shots['First Time'].map({True: '✓', False: ''})
    display_shots['1v1'] = display_shots['1v1'].map({True: '✓', False: ''})
    display_shots['Pressure'] = display_shots['Pressure'].map({True: '✓', False: ''})
    display_shots['In Box'] = display_shots['In Box'].map({True: '✓', False: ''})
    display_shots['Goal'] = display_shots['Goal'].map({1: '⚽', 0: ''})
    
    # Round numerical columns
    display_shots['Distance (m)'] = display_shots['Distance (m)'].round(1)
    display_shots['Angle (rad)'] = display_shots['Angle (rad)'].round(2)
    
    # Show summary stats
    col_stat1, col_stat2, col_stat3, col_stat4 = st.columns(4)
    with col_stat1:
        avg_dist = player_shots['shot_distance'].mean()
        st.metric("Avg Distance", f"{avg_dist:.1f}m")
    with col_stat2:
        conv_rate = (player_shots['is_goal'].sum() / len(player_shots)) * 100
        st.metric("Conversion Rate", f"{conv_rate:.1f}%")
    with col_stat3:
        first_time_pct = (player_shots['shot_first_time'].sum() / len(player_shots)) * 100
        st.metric("First Time %", f"{first_time_pct:.0f}%")
    with col_stat4:
        box_pct = (player_shots['within_penalty_area'].sum() / len(player_shots)) * 100
        st.metric("In Box %", f"{box_pct:.0f}%")
    
    # Show table
    st.dataframe(
        display_shots,
        use_container_width=True,
        height=400
    )
else:
    st.warning("No shot data available for this player")
st.markdown("---")

# Specialization analysis
st.subheader("Specialization Profile")
st.caption("What makes this player unique?")

# Calculate deltas from global
deltas = player_coeffs - global_betas

# Find top strengths and weaknesses
strengths_idx = np.argsort(deltas)[-5:][::-1]  # Top 5
weaknesses_idx = np.argsort(deltas)[:5]  # Bottom 5

col_strength, col_weakness = st.columns(2)

with col_strength:
    st.markdown("**💪 Top Strengths** (vs population)")
    for idx in strengths_idx:
        delta_val = deltas[idx]
        if delta_val > 0.1:  # Only show meaningful positives
            st.markdown(f"- **{feature_names[idx]}**: +{delta_val:.3f}")

with col_weakness:
    st.markdown("**📉 Relative Weaknesses** (vs population)")
    for idx in weaknesses_idx:
        delta_val = deltas[idx]
        if delta_val < -0.1:  # Only show meaningful negatives
            st.markdown(f"- **{feature_names[idx]}**: {delta_val:.3f}")

st.markdown("---")
# Footer
from utils.footer import render_footer
render_footer()