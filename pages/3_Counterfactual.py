import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from utils.data_loader import load_player_mapping, load_bayesian_data, load_shots_data
from utils.feature_engineering import build_bayesian_features
from utils.bayesian_engine import predict_bayesian_xg
from utils.plotly_theme import COLORS
import plotly.io as pio
pio.templates.default = 'xg_dark'

st.set_page_config(page_title="Counterfactual Simulator", page_icon="🔄", layout="wide")

st.title("🔄 Counterfactual Simulator")
st.markdown("Answer the question: *What if Player B took Player A's shots?*")

# Load data
player_mapping = load_player_mapping()
bayesian_data = load_bayesian_data()
shots_data = load_shots_data()

player_names = sorted(player_mapping['player_name'].tolist())

st.markdown("---")

# Swap button handler
def swap_players():
    st.session_state.player_a, st.session_state.player_b = st.session_state.player_b, st.session_state.player_a

# Initialize defaults with placeholders
if 'player_a' not in st.session_state:
    st.session_state.player_a = "-- Select Player A --"
if 'player_b' not in st.session_state:
    st.session_state.player_b = "-- Select Player B --"

# Add placeholder options
player_options_a = ["-- Select Player A --"] + player_names
player_options_b = ["-- Select Player B --"] + player_names

# Swap button centered
col_left, col_center, col_right = st.columns([4, 2, 4])
with col_center:
    st.button("🔄 Swap Players", on_click=swap_players, use_container_width=True)

st.markdown("<br>", unsafe_allow_html=True)

# Player selection
col1, col2 = st.columns(2)

with col1:
    st.subheader("Player A: Shot Provider")
    st.selectbox(
        "Whose shots do we analyze?",
        options=player_options_a,
        key='player_a'
    )

with col2:
    st.subheader("Player B: Ability Provider")
    st.selectbox(
        "Whose finishing ability do we apply?",
        options=player_options_b,
        key='player_b'
    )

# Get values from session state FIRST
player_a = st.session_state.player_a
player_b = st.session_state.player_b

# Check if valid players selected
if player_a == "-- Select Player A --" or player_b == "-- Select Player B --":
    st.info("👆 Select both players above to run counterfactual analysis")
    st.stop()

# SPINNER starts here - wraps ALL analysis code
with st.spinner(f"Running counterfactual: {player_a} shots with {player_b} ability..."):
    # Error handling
    try:
        player_a_id = player_mapping[player_mapping['player_name'] == player_a]['player_id'].values[0]
    except (IndexError, KeyError):
        st.error(f"❌ Player '{player_a}' not found in dataset.")
        st.stop()
    
    player_a_shots = shots_data[shots_data['player_id'] == player_a_id].copy()
    
    if len(player_a_shots) == 0:
        st.warning(f"⚠️ {player_a} has no shots in the dataset (2015-16 season).")
        st.info("This player may not have played enough minutes or was not in the dataset. Try selecting a different player.")
        st.stop()
    
    st.markdown("---")

# Simulate button
if st.button("🔄 RUN COUNTERFACTUAL ANALYSIS", type="primary", use_container_width=True):
    
    # Get Player A's shots with error handling
    try:
        player_a_id = player_mapping[player_mapping['player_name'] == player_a]['player_id'].values[0]
    except (IndexError, KeyError):
        st.error(f"❌ Player '{player_a}' not found in dataset.")
        st.stop()
    
    player_a_shots = shots_data[shots_data['player_id'] == player_a_id].copy()
    
    if len(player_a_shots) == 0:
        st.warning(f" {player_a} has no shots in the dataset (2015-16 season).")
        st.info("This player may not have played enough minutes or was not in the dataset. Try selecting a different player.")
        st.stop()
    else:
        st.success(f" Analyzing {len(player_a_shots)} shots from **{player_a}**")
        
        # Calculate xG for each shot using both players
        player_a_xg_list = []
        player_b_xg_list = []
        
        with st.spinner("Computing counterfactual xG values..."):
            for idx, shot in player_a_shots.iterrows():
                # Rebuild feature vector for this shot
                features = build_bayesian_features(
                    shot['shot_distance'],
                    shot['gk_distance'],
                    shot['shot_angle'],
                    shot['shot_body_part'],
                    shot['shot_technique'],
                    shot['shot_first_time'],
                    shot['shot_one_on_one'],
                    shot['under_pressure'],
                    shot['within_penalty_area'],
                    shot['num_defenders_in_triangle']
                )
                
                # Get xG from both players
                xg_a = predict_bayesian_xg(player_a, features, bayesian_data)
                xg_b = predict_bayesian_xg(player_b, features, bayesian_data)
                
                player_a_xg_list.append(xg_a)
                player_b_xg_list.append(xg_b)
        
        # Calculate totals
        total_a = sum(player_a_xg_list)
        total_b = sum(player_b_xg_list)
        delta = total_b - total_a
        actual_goals = player_a_shots['is_goal'].sum()
        
        # Display results
        st.markdown("---")
        st.subheader("📊 Results")
        
        col_res1, col_res2, col_res3, col_res4 = st.columns(4)
        
        with col_res1:
            st.metric(f"{player_a} Expected", f"{total_a:.2f} goals")
            st.caption("Using their own ability")
        
        with col_res2:
            st.metric(f"{player_b} Expected", f"{total_b:.2f} goals")
            st.caption("Using their ability on A's shots")
        
        with col_res3:
            delta_color = "off" if delta < 0 else "normal"
            st.metric("Delta", f"{delta:+.2f} goals", delta_color=delta_color)
            st.caption("Difference (B - A)")
        
        with col_res4:
            st.metric("Actual Goals Scored", f"{int(actual_goals)}")
            st.caption(f"By {player_a} in reality")
        
        st.markdown("---")
        
        # Interpretation
        if abs(delta) < 1:
            interpretation = f"**Minimal difference.** {player_b} and {player_a} would produce similar outcomes from these shots."
        elif delta > 0:
            interpretation = f"**{player_b} would score ~{delta:.1f} more goals** from {player_a}'s exact shot selection. Their finishing ability is better suited to these situations."
        else:
            interpretation = f"**{player_a} would score ~{abs(delta):.1f} more goals** than {player_b} from these shots. {player_a}'s ability is better suited to their own shot selection."
        
        st.info(interpretation)
        
        st.markdown("---")
        
        # Shot-by-shot breakdown
        st.subheader("📋 Shot-by-Shot Analysis")
        
        # Build comparison table
        comparison_df = player_a_shots[[
            'shot_distance', 'shot_angle', 'shot_body_part', 'shot_technique',
            'shot_one_on_one', 'within_penalty_area', 'num_defenders_in_triangle', 'is_goal'
        ]].copy()
        
        comparison_df['xG_A'] = player_a_xg_list
        comparison_df['xG_B'] = player_b_xg_list
        comparison_df['Delta'] = [b - a for a, b in zip(player_a_xg_list, player_b_xg_list)]
        
        # Rename for display
        comparison_df.columns = [
            'Distance', 'Angle', 'Body', 'Tech', '1v1', 'Box', 'Def', 'Goal',
            f'{player_a} xG', f'{player_b} xG', 'Δ'
        ]
        
        # Format
        comparison_df['Distance'] = comparison_df['Distance'].round(1)
        comparison_df['Angle'] = comparison_df['Angle'].round(2)
        comparison_df['1v1'] = comparison_df['1v1'].map({True: '✓', False: ''})
        comparison_df['Box'] = comparison_df['Box'].map({True: '✓', False: ''})
        comparison_df['Goal'] = comparison_df['Goal'].map({1: '⚽', 0: ''})
        comparison_df[f'{player_a} xG'] = comparison_df[f'{player_a} xG'].round(3)
        comparison_df[f'{player_b} xG'] = comparison_df[f'{player_b} xG'].round(3)
        comparison_df['Δ'] = comparison_df['Δ'].round(3)
        
        # Summary stats
        col_table1, col_table2, col_table3 = st.columns(3)
        with col_table1:
            favorable = sum(1 for d in player_b_xg_list if d > player_a_xg_list[player_b_xg_list.index(d)])
            st.metric("Shots Favoring B", f"{favorable}/{len(player_a_shots)}")
        with col_table2:
            avg_delta = np.mean([b - a for a, b in zip(player_a_xg_list, player_b_xg_list)])
            st.metric("Avg Delta per Shot", f"{avg_delta:+.3f}")
        with col_table3:
            max_delta = max([abs(b - a) for a, b in zip(player_a_xg_list, player_b_xg_list)])
            st.metric("Max Difference", f"{max_delta:.3f}")
        
        st.dataframe(comparison_df, use_container_width=True, height=400)
        st.markdown("---")
        
        # Posterior distribution comparison
        st.subheader("📊 Posterior Distribution Comparison")
        st.caption("Uncertainty-aware comparison of total expected goals")
        
        from utils.bayesian_engine import predict_bayesian_xg_with_uncertainty
        from scipy.stats import gaussian_kde
        with st.expander("ℹ️ How to read this chart"):
            st.markdown(f"""
            - **X-axis**: xG if {player_a} takes the shot
            - **Y-axis**: xG if {player_b} takes the shot
            - **Yellow diagonal line**: Equal ability (both players equally good)
            - **Green points**: {player_b} is better suited (above diagonal)
            - **Red points**: {player_a} is better suited (below diagonal)
            
            Points far from the diagonal show shots where one player has a clear advantage.
            """)
        
        st.markdown("---")
        
        # Posterior distribution comparison
        st.subheader("📊 Posterior Distribution Comparison")
        st.caption("Uncertainty-aware comparison of total expected goals")
        
        from utils.bayesian_engine import predict_bayesian_xg_with_uncertainty
        from scipy.stats import gaussian_kde
        
        # Sample from posterior for both players across all shots
        with st.spinner("Sampling from posterior distributions..."):
            n_samples = 1000
            total_a_samples = np.zeros(n_samples)
            total_b_samples = np.zeros(n_samples)
            
            for idx, shot in player_a_shots.iterrows():
                features = build_bayesian_features(
                    shot['shot_distance'], shot['gk_distance'], shot['shot_angle'],
                    shot['shot_body_part'], shot['shot_technique'],
                    shot['shot_first_time'], shot['shot_one_on_one'],
                    shot['under_pressure'], shot['within_penalty_area'],
                    shot['num_defenders_in_triangle']
                )
                
                # Get samples for both players
                _, _, _, samples_a = predict_bayesian_xg_with_uncertainty(player_a, features, bayesian_data)
                _, _, _, samples_b = predict_bayesian_xg_with_uncertainty(player_b, features, bayesian_data)
                
                total_a_samples += samples_a
                total_b_samples += samples_b
        
        # Create KDE curves
        kde_a = gaussian_kde(total_a_samples)
        kde_b = gaussian_kde(total_b_samples)
        
        x_min = min(total_a_samples.min(), total_b_samples.min()) - 2
        x_max = max(total_a_samples.max(), total_b_samples.max()) + 2
        x_range = np.linspace(x_min, x_max, 300)
        
        density_a = kde_a(x_range)
        density_b = kde_b(x_range)
        
        # Calculate credible intervals
        ci_a_lower, ci_a_upper = np.percentile(total_a_samples, [2.5, 97.5])
        ci_b_lower, ci_b_upper = np.percentile(total_b_samples, [2.5, 97.5])
        
        # Plot
        fig_kde = go.Figure()
        
        # Player A distribution
        fig_kde.add_trace(go.Scatter(
            x=x_range, y=density_a,
            fill='tozeroy',
            fillcolor='rgba(59, 130, 246, 0.3)',
            line=dict(color=COLORS['xg_blue'], width=3),
            name=f'{player_a} — mean={total_a:.1f}, 95% HDI=[{ci_a_lower:.1f}, {ci_a_upper:.1f}]'
        ))
        
        # Player B distribution
        fig_kde.add_trace(go.Scatter(
            x=x_range, y=density_b,
            fill='tozeroy',
            fillcolor='rgba(255, 107, 53, 0.3)',
            line=dict(color=COLORS['shot_gold'], width=3),
            name=f'{player_b} — mean={total_b:.1f}, 95% HDI=[{ci_b_lower:.1f}, {ci_b_upper:.1f}]'
        ))
        
        # Mean lines
        fig_kde.add_vline(x=total_a, line_dash="dash", line_color=COLORS['xg_blue'], line_width=2,
                         annotation_text=f"μ={total_a:.1f}", annotation_position="top")
        fig_kde.add_vline(x=total_b, line_dash="dash", line_color=COLORS['shot_gold'], line_width=2,
                         annotation_text=f"μ={total_b:.1f}", annotation_position="top")
        
        fig_kde.update_layout(
            title=f"{player_a} vs {player_b} (Posterior KDE Comparison)",
            xaxis_title="Total Expected Goals (xG)",
            yaxis_title="Probability Density (1/xG)",
            height=450,
            plot_bgcolor='#0A0F1E',
            paper_bgcolor='#0A0F1E',
            font=dict(color='#E8EDF5'),
            xaxis=dict(gridcolor='#1E2D45'),
            yaxis=dict(gridcolor='#1E2D45', showticklabels=False),
            legend=dict(bgcolor='#0A0F1E', font=dict(color='#E8EDF5'))
        )
        
        st.plotly_chart(fig_kde, use_container_width=True)
        
        with st.expander("ℹ️ Understanding this visualization"):
            st.markdown(f"""
            This shows the **full uncertainty** around the total expected goals for each player.
            
            - **Cyan curve**: {player_a}'s posterior distribution
            - **Orange curve**: {player_b}'s posterior distribution
            - **Dashed lines**: Mean (μ) expected goals
            - **95% HDI**: Highest Density Interval (credible interval)
            
            **Key insight**: If the curves don't overlap much, we're highly confident one player 
            would outscore the other. If they overlap significantly, the outcome is uncertain.
            
            In this case: {ci_a_lower:.1f} to {ci_a_upper:.1f} goals for {player_a}, 
            vs {ci_b_lower:.1f} to {ci_b_upper:.1f} goals for {player_b}.
            """)

else:
    st.info("👆 Select two players and click **RUN COUNTERFACTUAL ANALYSIS**")
# Footer
from utils.footer import render_footer
render_footer()
