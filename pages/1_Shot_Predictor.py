import streamlit as st
from utils.data_loader import load_player_mapping, load_preferred_foot
from utils.feature_engineering import BODY_PART_OPTIONS, TECHNIQUE_OPTIONS
from utils.plotly_theme import COLORS
import plotly.io as pio
pio.templates.default = 'xg_dark'

st.set_page_config(page_title="Shot Predictor", page_icon="⚽", layout="wide")

st.title("⚽ Shot Predictor")
st.markdown("Build a shot scenario and compare Bayesian vs XGBoost predictions")

# Load data
player_mapping = load_player_mapping()
player_names = sorted(player_mapping['player_name'].tolist())
preferred_foot_lookup = load_preferred_foot()

st.markdown("---")

# ═══════════════════════════════════════════════════════════════
# CENTERED MAIN AREA — ALL INPUTS
# ═══════════════════════════════════════════════════════════════

_, center, _ = st.columns([1, 2, 1])

with center:

    # ── Player ──────────────────────────────────────────────────
    st.header("⚙️ Shot Configuration")
    st.subheader("Player")

    player_options = ["-- Select a player --"] + player_names
    selected_player = st.selectbox(
        "Choose Player:",
        options=player_options,
        index=0
    )

    if selected_player == "-- Select a player --":
        st.info("Select a player above to begin analysis")
        st.stop()

    st.markdown("---")

    # ── Quick Scenarios ─────────────────────────────────────────
    st.subheader("⚡ Quick Scenarios")
    col_preset1, col_preset2 = st.columns(2)

    presets = {
        "Penalty": {
            "distance": 11.0, "gk_distance": 0.1, "angle": 90,
            "body_part": "Right Foot", "technique": "Normal",
            "first_time": False, "one_on_one": False,
            "pressure": False,
            "in_penalty_area": True, "num_defenders": 0
        },
        "1v1 Break": {
            "distance": 8.0, "gk_distance": 3.0, "angle": 55,
            "body_part": "Right Foot", "technique": "Normal",
            "first_time": False, "one_on_one": True, "pressure": False,
            "in_penalty_area": True, "num_defenders": 0
        },
        "Edge of Box": {
            "distance": 16.5, "gk_distance": 5.0, "angle": 35,
            "body_part": "Right Foot", "technique": "Normal",
            "first_time": False, "one_on_one": False, "pressure": False,
            "in_penalty_area": True, "num_defenders": 2
        },
        "Long Range": {
            "distance": 28.0, "gk_distance": 3.0, "angle": 15,
            "body_part": "Right Foot", "technique": "Normal",
            "first_time": False, "one_on_one": False, "pressure": False,
            "in_penalty_area": False, "num_defenders": 4
        },
        "Header": {
            "distance": 7.0, "gk_distance": 2.0, "angle": 50,
            "body_part": "Head", "technique": "Normal",
            "first_time": False, "one_on_one": False, "pressure": False,
            "in_penalty_area": True, "num_defenders": 1
        },
        "First Touch": {
            "distance": 12.0, "gk_distance": 4.5, "angle": 45,
            "body_part": "Right Foot", "technique": "Normal",
            "first_time": True, "one_on_one": False, "pressure": False,
            "in_penalty_area": True, "num_defenders": 1
        }
    }

    preset_buttons = list(presets.keys())
    active = st.session_state.get('preset', None)

    with col_preset1:
        if st.button(preset_buttons[0], use_container_width=True,
                     type="primary" if active == preset_buttons[0] else "secondary"):
            st.session_state.preset = preset_buttons[0]
            st.session_state.checkbox_penalty_area = True
            st.rerun()
        if st.button(preset_buttons[2], use_container_width=True,
                     type="primary" if active == preset_buttons[2] else "secondary"):
            st.session_state.preset = preset_buttons[2]
            st.session_state.checkbox_penalty_area = True
            st.rerun()
        if st.button(preset_buttons[4], use_container_width=True,
                     type="primary" if active == preset_buttons[4] else "secondary"):
            st.session_state.preset = preset_buttons[4]
            st.session_state.checkbox_penalty_area = True
            st.rerun()

    with col_preset2:
        if st.button(preset_buttons[1], use_container_width=True,
                     type="primary" if active == preset_buttons[1] else "secondary"):
            st.session_state.preset = preset_buttons[1]
            st.session_state.checkbox_penalty_area = True
            st.rerun()
        if st.button(preset_buttons[3], use_container_width=True,
                     type="primary" if active == preset_buttons[3] else "secondary"):
            st.session_state.preset = preset_buttons[3]
            st.session_state.checkbox_penalty_area = False
            st.rerun()
        if st.button(preset_buttons[5], use_container_width=True,
                     type="primary" if active == preset_buttons[5] else "secondary"):
            st.session_state.preset = preset_buttons[5]
            st.session_state.checkbox_penalty_area = True
            st.rerun()

    # Apply preset if selected
    if 'preset' in st.session_state and st.session_state.preset in presets:
        active_preset = presets[st.session_state.preset]
    else:
        active_preset = None

    # Clear preset button
    if active_preset:
        if st.button("✖ Clear Preset", use_container_width=True, type="secondary"):
            st.session_state.preset = None
            st.rerun()

    st.markdown("---")

    # ── Shot Location ────────────────────────────────────────────
    st.subheader(" Shot Location")
    col1, col2 = st.columns(2)
    with col1:
        shot_distance = st.number_input("Distance (m)", 1.0, 40.0,
            active_preset["distance"] if active_preset else 20.0, 0.5,
            disabled=active_preset is not None)
    with col2:
        gk_distance = st.number_input("GK Distance (m)", 0.0, 20.0,
            active_preset["gk_distance"] if active_preset else 5.0, 0.5,
            disabled=active_preset is not None)

    shot_angle_deg = st.slider("Angle (degrees)", 0, 90,
        active_preset["angle"] if active_preset else 30, 5,
        disabled=st.session_state.get('preset') == "Penalty")
    shot_angle = shot_angle_deg * (3.14159 / 180)

    shot_angle = shot_angle_deg * (3.14159 / 180)

    # Mini-pitch angle visualization
    import math
    t = shot_angle_deg / 90
    player_x = 70 + t * 30
    player_y = 25 + t * 65
    goal_left_x = 70
    goal_right_x = 130
    goal_y = 18

    st.markdown(f"""
    <div style="display:flex; justify-content:center; padding:4px 0;">
    <svg width="220" height="105" viewBox="0 0 220 105">
        <rect x="5" y="5" width="210" height="95" rx="6" fill="#0D1F17" stroke="#10B981" stroke-width="1.5" opacity="0.6"/>
        <rect x="{goal_left_x}" y="{goal_y - 5}" width="{goal_right_x - goal_left_x}" height="10" rx="3" fill="#F9FAFB" opacity="0.95"/>
        <polygon points="{player_x},{player_y} {goal_left_x},{goal_y} {goal_right_x},{goal_y}" 
            fill="#FFD700" fill-opacity="0.18" stroke="none"/>
        <line x1="{player_x}" y1="{player_y}" x2="{goal_left_x}" y2="{goal_y}" 
            stroke="#FFD700" stroke-width="2.5" stroke-dasharray="6 4" opacity="0.8"/>
        <line x1="{player_x}" y1="{player_y}" x2="{goal_right_x}" y2="{goal_y}" 
            stroke="#FFD700" stroke-width="2.5" stroke-dasharray="6 4" opacity="0.8"/>
        <circle cx="{player_x}" cy="{player_y}" r="7" fill="#FF6B35" stroke="white" stroke-width="2.5"/>
        <text x="{player_x + 14}" y="{player_y + 5}" text-anchor="start" fill="#FFD700" font-size="15" font-weight="700">{shot_angle_deg}°</text>
        <text x="100" y="{goal_y + 2}" text-anchor="middle" fill="#0A0E1A" font-size="9" font-weight="700">GOAL</text>
    </svg>
    </div>
    """, unsafe_allow_html=True)

    # Input validation
    if shot_distance < 2.0:
        st.warning("⚠️ Distance < 2m is extremely close. Adjust if needed.")
    if shot_distance > 35.0:
        st.warning("⚠️ Distance > 35m is very rare. Check your input.")
    if gk_distance > shot_distance:
        st.error("❌ Goalkeeper can't be further from goal than the ball!")
        st.stop()
    if shot_angle_deg == 0:
        st.info("ℹ️ 0° angle = tight angle near post")

    st.markdown("---")

    # ── Shot Mechanics ────────────────────────────────────────────
    st.subheader(" Shot Mechanics")

    if active_preset:
        body_part_default = active_preset["body_part"]
    else:
        preferred_foot = preferred_foot_lookup.get(selected_player, "Right")
        body_part_default = f"{preferred_foot} Foot"

    body_part = st.selectbox("Body Part:", BODY_PART_OPTIONS,
        index=BODY_PART_OPTIONS.index(body_part_default))

    if not active_preset:
        st.caption(f"ℹ️ Auto-selected {preferred_foot} Foot based on player data. You can change it to explore different scenarios.")

    if body_part == "Head":
        allowed_techniques = ["Normal", "Diving Header"]
    elif body_part == "Other":
        allowed_techniques = ["Normal"]
    elif active_preset and st.session_state.preset == "Penalty":
        allowed_techniques = ["Normal"]
    else:
        allowed_techniques = ["Normal", "Half Volley", "Volley", "Lob", "Overhead Kick", "Backheel"]

    if active_preset and active_preset["technique"] in allowed_techniques:
        tech_default = allowed_techniques.index(active_preset["technique"])
    else:
        tech_default = 0

    technique = st.selectbox("Technique:", allowed_techniques, index=tech_default)

    if body_part == "Head":
        st.caption("ℹ️ Technique options filtered for headers")

    st.markdown("---")

    # ── Situation ─────────────────────────────────────────────────
    st.subheader("⚡ Situation")

    if "checkbox_penalty_area" not in st.session_state:
        st.session_state.checkbox_penalty_area = False

    if active_preset:
        st.session_state.checkbox_penalty_area = active_preset["in_penalty_area"]
    elif shot_distance <= 16.5:
        st.session_state.checkbox_penalty_area = True
    elif shot_distance > 16.5:
        st.session_state.checkbox_penalty_area = False

    in_penalty_area = st.checkbox(
        "In Penalty Area",
        help="Auto-updates based on distance (≤16.5m = in box)",
        key="checkbox_penalty_area"
    )
    if in_penalty_area and shot_distance > 16.5:
        st.warning("⚠️ Distance > 16.5m but marked as in box")
    elif not in_penalty_area and shot_distance <= 16.5:
        st.info("ℹ️ Distance ≤ 16.5m but marked outside box")

    col3, col4 = st.columns(2)
    with col3:
        first_time = st.checkbox("First Time",
            value=active_preset["first_time"] if active_preset else False,
            key="checkbox_first_time",
            disabled=active_preset is not None)
        one_on_one = st.checkbox("One-on-One",
            value=active_preset["one_on_one"] if active_preset else False,
            key="checkbox_one_on_one",
            disabled=active_preset is not None)
    with col4:
        pressure = st.checkbox("Under Pressure",
            value=active_preset["pressure"] if active_preset else False,
            key="checkbox_pressure",
            disabled=active_preset is not None)

    if active_preset:
        default_defenders = active_preset["num_defenders"]
    else:
        if shot_distance > 23:
            default_defenders = 4
        elif shot_distance > 20:
            default_defenders = 3
        elif shot_distance > 16.5:
            default_defenders = 2
        else:
            default_defenders = 1

    num_defenders = st.slider("Defenders:", 0, 5, default_defenders,
        disabled=active_preset is not None)

    if one_on_one and num_defenders > 0:
        st.error("⚠️ One-on-One means NO defenders. Set defenders to 0 or uncheck One-on-One.")
        st.stop()
    if pressure and num_defenders == 0:
        st.warning("⚠️ 'Under Pressure' typically implies defenders nearby. Consider adding defenders.")

    st.markdown("---")

    # ── Calculate Button ──────────────────────────────────────────
    calculate_btn = st.button("⚽ CALCULATE xG", type="primary", use_container_width=True)

# ═══════════════════════════════════════════════════════════════
# MAIN AREA — RESULTS
# ═══════════════════════════════════════════════════════════════

if calculate_btn:
    with st.spinner("Calculating xG predictions..."):
        from utils.data_loader import load_bayesian_data, load_xgboost_model
        from utils.feature_engineering import build_bayesian_features, build_xgboost_features
        from utils.bayesian_engine import predict_bayesian_xg, predict_bayesian_xg_with_uncertainty
        from utils.xgboost_engine import predict_xgboost_xg

    bayesian_data = load_bayesian_data()
    xgboost_model = load_xgboost_model()

    bayes_features = build_bayesian_features(
        shot_distance, gk_distance, shot_angle,
        body_part, technique,
        first_time, one_on_one, pressure,
        in_penalty_area, num_defenders
    )

    xgb_features = build_xgboost_features(
        shot_distance, gk_distance, shot_angle,
        body_part, technique,
        first_time, one_on_one, pressure,
        in_penalty_area, num_defenders
    )

    bayes_xg, lower, upper, xg_samples = predict_bayesian_xg_with_uncertainty(
        selected_player, bayes_features, bayesian_data
    )
    xgb_xg = predict_xgboost_xg(xgboost_model, xgb_features)
    delta = bayes_xg - xgb_xg

    st.success(f"✅ Analysis Complete for **{selected_player}**")

    col_left, col_mid, col_right = st.columns(3)

    with col_left:
        st.metric("🔵 Bayesian xG", f"{bayes_xg:.3f}")
        st.caption(f"95% CI: [{lower:.3f}, {upper:.3f}]")
        st.caption("Player-specific model")

    with col_mid:
        st.metric("🟠 XGBoost xG", f"{xgb_xg:.3f}")
        st.caption("Population average")

    with col_right:
        delta_color = "normal" if abs(delta) < 0.02 else ("off" if delta < 0 else "inverse")
        st.metric("📊 Delta", f"{delta:+.3f}", delta_color=delta_color)
        st.caption("Bayesian - XGBoost")

    st.markdown("---")

    st.subheader(" Shot Visualization")

    from mplsoccer import Pitch
    import matplotlib.pyplot as plt
    import numpy as np

    fig, ax = plt.subplots(figsize=(12, 8), facecolor='#10B981')

    pitch = Pitch(
        pitch_type='statsbomb',
        pitch_color='#10B981',
        line_color='white',
        linewidth=2.5,
        goal_type='box',
        stripe=False
    )
    pitch.draw(ax=ax)

    shot_x = 120 - shot_distance
    t = shot_angle_deg / 90
    shot_y = 15 + t * 25
    goal_x = 120
    goal_y = 40

    gk_x = 120 - gk_distance
    pitch.scatter(gk_x, goal_y, ax=ax, c='#FF4757', s=80,
                 edgecolors='white', linewidth=2, zorder=4,
                 marker='o', label='Goalkeeper')

    if num_defenders > 0:
        def_y_center = (shot_y + 40) / 2

        if num_defenders == 1:
            defender_positions = [(shot_x + (gk_x - shot_x) * 0.6, def_y_center)]
        elif num_defenders == 2:
            defender_positions = [
                (shot_x + (gk_x - shot_x) * 0.5, def_y_center - 2),
                (shot_x + (gk_x - shot_x) * 0.5, def_y_center + 2)
            ]
        elif num_defenders == 3:
            defender_positions = [
                (shot_x + (gk_x - shot_x) * 0.5, def_y_center),
                (shot_x + (gk_x - shot_x) * 0.6, def_y_center - 3),
                (shot_x + (gk_x - shot_x) * 0.6, def_y_center + 3)
            ]
        elif num_defenders == 4:
            defender_positions = [
                (shot_x + (gk_x - shot_x) * 0.5, def_y_center - 2),
                (shot_x + (gk_x - shot_x) * 0.5, def_y_center + 2),
                (shot_x + (gk_x - shot_x) * 0.65, def_y_center - 4),
                (shot_x + (gk_x - shot_x) * 0.65, def_y_center + 4)
            ]
        else:
            defender_positions = [
                (shot_x + (gk_x - shot_x) * 0.5, def_y_center),
                (shot_x + (gk_x - shot_x) * 0.5, def_y_center - 3),
                (shot_x + (gk_x - shot_x) * 0.5, def_y_center + 3),
                (shot_x + (gk_x - shot_x) * 0.65, def_y_center - 5),
                (shot_x + (gk_x - shot_x) * 0.65, def_y_center + 5)
            ]

        def_x = [pos[0] for pos in defender_positions]
        def_y = [pos[1] for pos in defender_positions]
        pitch.scatter(def_x, def_y, ax=ax, c='#3742fa', s=120,
                     edgecolors='white', linewidth=2, zorder=3,
                     label=f'{num_defenders} Defender(s)')

    cone_near = 36
    cone_far = 44

    ax.plot([shot_x, goal_x], [shot_y, cone_near],
           color='#FFD700', linewidth=2, linestyle='--', alpha=0.6, zorder=1)
    ax.plot([shot_x, goal_x], [shot_y, cone_far],
           color='#FFD700', linewidth=2, linestyle='--', alpha=0.6, zorder=1)

    angle_x = [shot_x, goal_x, goal_x, shot_x]
    angle_y = [shot_y, cone_near, cone_far, shot_y]
    ax.fill(angle_x, angle_y, color='#FFD700', alpha=0.15, zorder=1)

    pitch.scatter(shot_x, shot_y, ax=ax, c='#FF6B35', s=200,
                 edgecolors='white', linewidth=3, zorder=5, alpha=1)

    ax.text(shot_x, shot_y-6, f"xG: {bayes_xg:.2f}",
           ha='center', va='top', fontsize=12, color='white',
           fontweight='bold', bbox=dict(boxstyle='round',
           facecolor='#FF6B35', alpha=0.9, edgecolor='white', linewidth=2))

    ax.text(shot_x, shot_y+6, f"{shot_distance:.1f}m",
           ha='center', va='bottom', fontsize=10, color='white',
           bbox=dict(boxstyle='round', facecolor='#0A0F1E', alpha=0.7))

    ax.text(shot_x+5, shot_y, f"∠{shot_angle_deg}°",
           ha='left', va='center', fontsize=9, color='#FFD700',
           bbox=dict(boxstyle='round', facecolor='#0A0F1E', alpha=0.7))

    ax.legend(loc='upper left', framealpha=0.9, facecolor='#0A0F1E',
             edgecolor='white', labelcolor='white')
    ax.set_facecolor('#10B981')
    fig.patch.set_facecolor('#10B981')
    st.pyplot(fig)

    st.markdown("---")

    st.subheader("Feature Impact Analysis")
    st.caption("How each factor influenced the Bayesian xG prediction")

    from utils.bayesian_engine import get_feature_contributions
    import plotly.graph_objects as go

    contributions = get_feature_contributions(selected_player, bayes_features, bayesian_data)

    sorted_contribs = sorted(contributions.items(), key=lambda x: abs(x[1]), reverse=True)
    top_features = sorted_contribs[:10]
    feature_names = [f[0] for f in top_features]
    feature_values = [f[1] for f in top_features]

    colors = [COLORS['pitch_green'] if v > 0 else COLORS['miss_red'] for v in feature_values]

    fig_contrib = go.Figure(go.Bar(
        x=feature_values,
        y=feature_names,
        orientation='h',
        marker=dict(color=colors),
        text=[f"{v:+.3f}" for v in feature_values],
        textposition='outside',
    ))

    fig_contrib.update_layout(
        title="Top 10 Feature Contributions to Logit",
        xaxis_title="Contribution to Logit",
        yaxis_title="",
        height=400,
        plot_bgcolor='#0A0F1E',
        paper_bgcolor='#0A0F1E',
        font=dict(color='#E8EDF5'),
        xaxis=dict(gridcolor='#1E2D45', zerolinecolor='#00C4FF', zerolinewidth=2),
        yaxis=dict(gridcolor='#1E2D45'),
    )

    st.plotly_chart(fig_contrib, use_container_width=True)

    with st.expander("ℹ️ How to read this chart"):
        st.markdown("""
        - **Green bars** → factors that increased xG (positive contribution)
        - **Red bars** → factors that decreased xG (negative contribution)
        - **Longer bars** → stronger influence on the prediction
        
        The chart shows contributions to the **logit** (pre-sigmoid value). 
        Positive contributions push xG higher, negative contributions push it lower.
        """)

    st.markdown("---")

    st.subheader("📈 Bayesian Posterior Distribution")
    st.caption("Showing distribution of xG predictions from posterior samples")

    import plotly.graph_objects as go
    from scipy.stats import gaussian_kde

    kde = gaussian_kde(xg_samples)
    x_range = np.linspace(max(0, lower - 0.05), min(1, upper + 0.05), 300)
    density = kde(x_range)

    fig_dist = go.Figure()

    fig_dist.add_trace(go.Scatter(
        x=x_range,
        y=density,
        fill='tozeroy',
        fillcolor='rgba(59, 130, 246, 0.3)',
        line=dict(color=COLORS['xg_blue'], width=3),
        name='Posterior Density',
        mode='lines'
    ))

    fig_dist.add_vline(
        x=bayes_xg,
        line_dash="solid",
        line_color=COLORS['pitch_green'],
        line_width=3,
        annotation_text=f"μ = {bayes_xg:.3f}",
        annotation_position="top"
    )

    fig_dist.add_vline(
        x=lower,
        line_dash="dash",
        line_color=COLORS['shot_gold'],
        line_width=2,
        annotation_text=f"2.5%",
        annotation_position="bottom left"
    )

    fig_dist.add_vline(
        x=upper,
        line_dash="dash",
        line_color="#FFD700",
        line_width=2,
        annotation_text=f"97.5%",
        annotation_position="bottom right"
    )

    fig_dist.add_vrect(
        x0=lower, x1=upper,
        fillcolor="#FFD700", opacity=0.15,
        line_width=0
    )

    fig_dist.update_layout(
        xaxis_title="Expected Goals (xG)",
        yaxis_title="Probability Density",
        height=350,
        plot_bgcolor='#0A0F1E',
        paper_bgcolor='#0A0F1E',
        font=dict(color='#E8EDF5'),
        xaxis=dict(gridcolor='#1E2D45', range=[max(0, lower-0.05), min(1, upper+0.05)]),
        yaxis=dict(gridcolor='#1E2D45', showticklabels=False),
        showlegend=False
    )

    st.plotly_chart(fig_dist, use_container_width=True)

    col_info1, col_info2, col_info3 = st.columns(3)
    with col_info1:
        st.metric("Mean xG", f"{bayes_xg:.3f}")
    with col_info2:
        st.metric("95% Lower Bound", f"{lower:.3f}")
    with col_info3:
        st.metric("95% Upper Bound", f"{upper:.3f}")

    with st.expander("ℹ️ Understanding Uncertainty"):
        st.markdown("""
        This curve shows the **probability distribution** of xG values from the Bayesian model.
        
        - **Cyan curve**: Probability density — taller = more likely xG value
        - **Green solid line**: Mean (μ) — the expected xG
        - **Yellow dashed lines**: 95% credible interval boundaries
        - **Yellow shaded area**: 95% of the distribution falls here
        
        **Why does this matter?**  
        A narrow, tall curve → high confidence (consistent finishing ability).  
        A wide, flat curve → high uncertainty (limited data or inconsistent performance).
        
        XGBoost cannot provide this — it only gives a single point estimate.
        """)

else:
    st.info("Configure shot parameters above and click **CALCULATE xG**")

# Footer
from utils.footer import render_footer
render_footer()