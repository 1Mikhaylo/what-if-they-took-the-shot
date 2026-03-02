import streamlit as st

st.set_page_config(
    page_title="What If They Took The Shot?",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="collapsed"  
)

# Global fonts and styling


# Global fonts and styling
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Exo:wght@300;400;500;600;700&family=Roboto+Mono:wght@300;400;500;700&display=swap');
@import url('https://fonts.googleapis.com/icon?family=Material+Icons');
html, body, [class*="st-"] {
    font-family: 'Exo', sans-serif;
}
[data-testid="stMetricValue"],
[data-testid="stMetricDelta"],
code, pre {
    font-family: 'Roboto Mono', monospace;
}
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0F172A 0%, #0A0E1A 100%);
    border-right: 1px solid rgba(59, 130, 246, 0.2);
}
[data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3 {
    color: #3B82F6 !important;
}
[data-testid="stSidebarHeader"] {
    display: none !important;
}
[data-testid="collapsedControl"] {
    display: none !important;
}
[data-testid="collapsedControl"] div {
    display: none !important;
}
/* Exact fix for double_arrow_right icon text */
[data-testid="stIconMaterial"] {
    display: none !important;
}

/* ═══════════════════════════════════════════════ */
/* WELCOME CARD STYLES                            */
/* ═══════════════════════════════════════════════ */

.welcome-card {
    background: linear-gradient(145deg, #111827 0%, #0D1321 100%);
    border: 1px solid rgba(59, 130, 246, 0.15);
    border-radius: 16px;
    padding: 0;
    overflow: hidden;
    transition: all 0.3s ease;
    height: 100%;
}

.welcome-card:hover {
    border-color: rgba(59, 130, 246, 0.5);
    box-shadow: 0 8px 32px rgba(59, 130, 246, 0.15);
    transform: translateY(-4px);
}

.card-visual {
    width: 100%;
    height: 180px;
    display: flex;
    align-items: center;
    justify-content: center;
    position: relative;
    overflow: hidden;
}

.card-visual-shot {
    background: linear-gradient(135deg, #064E3B 0%, #0A0E1A 100%);
}

.card-visual-profile {
    background: linear-gradient(135deg, #1E1B4B 0%, #0A0E1A 100%);
}

.card-visual-counterfactual {
    background: linear-gradient(135deg, #7C2D12 0%, #0A0E1A 100%);
}

.card-body {
    padding: 24px;
}

.card-body h3 {
    font-family: 'Exo', sans-serif;
    font-size: 1.3rem;
    font-weight: 700;
    color: #F9FAFB;
    margin: 0 0 8px 0;
}

.card-body p {
    font-family: 'Exo', sans-serif;
    font-size: 0.95rem;
    color: #9CA3AF;
    margin: 0;
    line-height: 1.5;
}

.card-tag {
    display: inline-block;
    font-size: 0.7rem;
    font-weight: 600;
    letter-spacing: 1px;
    text-transform: uppercase;
    padding: 4px 10px;
    border-radius: 4px;
    margin-bottom: 12px;
}

.tag-bayesian {
    background: rgba(59, 130, 246, 0.15);
    color: #3B82F6;
}

.tag-analysis {
    background: rgba(139, 92, 246, 0.15);
    color: #8B5CF6;
}

.tag-counterfactual {
    background: rgba(255, 107, 53, 0.15);
    color: #FF6B35;
}

/* Make buttons stretch full width under cards */
.stButton > button {
    border-radius: 0 0 12px 12px;
}

/* Hide anchor link icons from headers */
h1 a, h2 a, h3 a, h4 a {
    display: none !important;
}

</style>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════
# HERO SECTION
# ═══════════════════════════════════════════════════════════════

st.markdown("""
<div style="display: flex; align-items: center; gap: 16px; margin-bottom: 24px;">
    <svg width="48" height="48" viewBox="0 0 56 56" fill="none">
        <rect width="56" height="56" rx="12" fill="#0D1F17"/>
        <rect x="10" y="4" width="36" height="24" rx="1" stroke="#10B981" stroke-width="1.2" fill="none" opacity="0.4"/>
        <line x1="20" y1="4" x2="36" y2="4" stroke="#F9FAFB" stroke-width="2.5" stroke-linecap="round"/>
        <rect x="18" y="4" width="20" height="10" rx="1" stroke="#10B981" stroke-width="0.8" fill="none" opacity="0.3"/>
        <circle cx="28" cy="22" r="1.5" fill="#10B981" opacity="0.5"/>
        <circle cx="28" cy="42" r="4" fill="#F9FAFB" opacity="0.9"/>
        <path d="M28 38 L22 10" stroke="#3B82F6" stroke-width="1.8" stroke-dasharray="3 2" stroke-linecap="round"/>
        <path d="M28 38 L34 10" stroke="#FF6B35" stroke-width="1.8" stroke-dasharray="3 2" stroke-linecap="round"/>
        <circle cx="22" cy="10" r="2.5" fill="#3B82F6" opacity="0.8"/>
        <circle cx="34" cy="10" r="2.5" fill="#FF6B35" opacity="0.8"/>
    </svg>
    <h1 style="margin: 0; font-size: 2.5rem; font-weight: 700; color: #F9FAFB;">
        What If They Took The Shot?
    </h1>
</div>
""", unsafe_allow_html=True)
st.markdown("### Hierarchical Bayesian xG — Player-Specific Finishing Analysis")
st.markdown("*Mahmudlu, Karakuş & Arkadaş (2025)*")
st.markdown("""
<p style="font-size: 1.1rem; color: #9CA3AF; margin: 16px 0 32px 0;">
    Explore how individual finishing ability changes expected goals — powered by Bayesian inference and Football Manager ratings.
</p>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════
# SIDEBAR CONTENT
# ═══════════════════════════════════════════════════════════════

st.sidebar.markdown("""
<div style="font-size:0.78rem; color:#9CA3AF; line-height:2;">
    📊 <b style="color:#F9FAFB;">148</b> players<br>
    ⚽ <b style="color:#F9FAFB;">9,970</b> shots<br>
    📅 <b style="color:#F9FAFB;">2015-16</b> season<br>
    🎮 <b style="color:#F9FAFB;">FM 2017</b> ratings
</div>
""", unsafe_allow_html=True)


st.sidebar.markdown("---")

# ═══════════════════════════════════════════════════════════════
# THREE FEATURE CARDS
# ═══════════════════════════════════════════════════════════════
col1, col2, col3 = st.columns(3, gap="medium")
# --- CARD 1: Shot Predictor ---
with col1:
    st.markdown("""
    <div class="welcome-card">
        <div class="card-visual card-visual-shot">
            <svg width="120" height="120" viewBox="0 0 120 120" fill="none" xmlns="http://www.w3.org/2000/svg">
                <!-- Pitch lines -->
                <rect x="10" y="20" width="100" height="80" rx="2" stroke="#10B981" stroke-width="1.5" fill="none" opacity="0.3"/>
                <line x1="60" y1="20" x2="60" y2="100" stroke="#10B981" stroke-width="1" opacity="0.3"/>
                <circle cx="60" cy="60" r="15" stroke="#10B981" stroke-width="1" fill="none" opacity="0.3"/>
                <!-- Crosshair -->
                <circle cx="75" cy="55" r="18" stroke="#3B82F6" stroke-width="2" fill="none" opacity="0.8"/>
                <circle cx="75" cy="55" r="10" stroke="#3B82F6" stroke-width="1.5" fill="none" opacity="0.5"/>
                <circle cx="75" cy="55" r="3" fill="#3B82F6" opacity="0.9"/>
                <line x1="75" y1="33" x2="75" y2="45" stroke="#3B82F6" stroke-width="1.5" opacity="0.6"/>
                <line x1="75" y1="65" x2="75" y2="77" stroke="#3B82F6" stroke-width="1.5" opacity="0.6"/>
                <line x1="53" y1="55" x2="65" y2="55" stroke="#3B82F6" stroke-width="1.5" opacity="0.6"/>
                <line x1="85" y1="55" x2="97" y2="55" stroke="#3B82F6" stroke-width="1.5" opacity="0.6"/>
                <!-- Shot trajectory -->
                <line x1="30" y1="70" x2="75" y2="55" stroke="#FF6B35" stroke-width="2" stroke-dasharray="4 3" opacity="0.7"/>
                <circle cx="30" cy="70" r="5" fill="#FF6B35" opacity="0.8"/>
            </svg>
        </div>
        <div class="card-body">
            <span class="card-tag tag-bayesian">Dual Engine</span>
            <h3>⚽ Shot Predictor</h3>
            <p>Build any shot scenario and compare player-specific Bayesian xG against population-level XGBoost predictions in real time.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("Launch Shot Predictor →", use_container_width=True, key="btn_shot"):
        st.switch_page("pages/1_Shot_Predictor.py")

# --- CARD 2: Player Profiles ---
with col2:
    st.markdown("""
    <div class="welcome-card">
        <div class="card-visual card-visual-profile">
            <svg width="120" height="120" viewBox="0 0 120 120" fill="none" xmlns="http://www.w3.org/2000/svg">
                <!-- Radar chart background -->
                <polygon points="60,20 95,40 95,80 60,100 25,80 25,40" stroke="#8B5CF6" stroke-width="1" fill="none" opacity="0.2"/>
                <polygon points="60,30 87,45 87,75 60,90 33,75 33,45" stroke="#8B5CF6" stroke-width="1" fill="none" opacity="0.15"/>
                <polygon points="60,40 80,50 80,70 60,80 40,70 40,50" stroke="#8B5CF6" stroke-width="1" fill="none" opacity="0.1"/>
                <!-- Radar data shape -->
                <polygon points="60,25 92,48 78,82 45,88 28,58 42,35" 
                    stroke="#8B5CF6" stroke-width="2" fill="#8B5CF6" fill-opacity="0.2"/>
                <!-- Axis lines -->
                <line x1="60" y1="20" x2="60" y2="100" stroke="#8B5CF6" stroke-width="0.5" opacity="0.3"/>
                <line x1="25" y1="40" x2="95" y2="80" stroke="#8B5CF6" stroke-width="0.5" opacity="0.3"/>
                <line x1="95" y1="40" x2="25" y2="80" stroke="#8B5CF6" stroke-width="0.5" opacity="0.3"/>
                <!-- Data points -->
                <circle cx="60" cy="25" r="3" fill="#8B5CF6" opacity="0.9"/>
                <circle cx="92" cy="48" r="3" fill="#8B5CF6" opacity="0.9"/>
                <circle cx="78" cy="82" r="3" fill="#8B5CF6" opacity="0.9"/>
                <circle cx="45" cy="88" r="3" fill="#8B5CF6" opacity="0.9"/>
                <circle cx="28" cy="58" r="3" fill="#8B5CF6" opacity="0.9"/>
                <circle cx="42" cy="35" r="3" fill="#8B5CF6" opacity="0.9"/>
                <!-- Person silhouette (small) -->
                <circle cx="60" cy="56" r="6" fill="#F9FAFB" opacity="0.6"/>
                <path d="M50 72 Q60 64 70 72" stroke="#F9FAFB" stroke-width="2" fill="none" opacity="0.4"/>
            </svg>
        </div>
        <div class="card-body">
            <span class="card-tag tag-analysis">17 Features</span>
            <h3>👤 Player Profiles</h3>
            <p>Discover each player's finishing fingerprint — radar charts, shot history, and specialization patterns across 148 players.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("Explore Player Profiles →", use_container_width=True, key="btn_profile"):
        st.switch_page("pages/2_Player_Profiles.py")

# --- CARD 3: Counterfactual ---
with col3:
    st.markdown("""
    <div class="welcome-card">
        <div class="card-visual card-visual-counterfactual">
            <svg width="120" height="120" viewBox="0 0 120 120" fill="none" xmlns="http://www.w3.org/2000/svg">
                <!-- Player A silhouette -->
                <circle cx="35" cy="42" r="8" fill="#3B82F6" opacity="0.7"/>
                <path d="M25 62 Q35 54 45 62 L45 72 L25 72 Z" fill="#3B82F6" opacity="0.5"/>
                <!-- Player B silhouette -->
                <circle cx="85" cy="42" r="8" fill="#FF6B35" opacity="0.7"/>
                <path d="M75 62 Q85 54 95 62 L95 72 L75 72 Z" fill="#FF6B35" opacity="0.5"/>
                <!-- Swap arrows -->
                <path d="M50 48 L70 48" stroke="#F9FAFB" stroke-width="2" opacity="0.8"/>
                <polygon points="68,44 76,48 68,52" fill="#F9FAFB" opacity="0.8"/>
                <path d="M70 58 L50 58" stroke="#F9FAFB" stroke-width="2" opacity="0.8"/>
                <polygon points="52,54 44,58 52,62" fill="#F9FAFB" opacity="0.8"/>
                <!-- Distribution curves -->
                <path d="M15 95 Q25 95 30 88 Q35 75 40 78 Q45 82 50 95" 
                    stroke="#3B82F6" stroke-width="1.5" fill="#3B82F6" fill-opacity="0.15"/>
                <path d="M70 95 Q75 95 80 85 Q85 72 90 76 Q95 80 105 95" 
                    stroke="#FF6B35" stroke-width="1.5" fill="#FF6B35" fill-opacity="0.15"/>
                <!-- "vs" label -->
                <text x="60" y="98" text-anchor="middle" fill="#F9FAFB" font-size="10" font-weight="600" opacity="0.5">vs</text>
            </svg>
        </div>
        <div class="card-body">
            <span class="card-tag tag-counterfactual">What-If</span>
            <h3>⇄ Counterfactual Simulator</h3>
            <p>Swap finishing abilities between players and see how outcomes change — with full posterior uncertainty analysis.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("Run Counterfactual Analysis →", use_container_width=True, key="btn_cf"):
        st.switch_page("pages/3_Counterfactual.py")

# ═══════════════════════════════════════════════════════════════
# BOTTOM SECTION
# ═══════════════════════════════════════════════════════════════

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<div style="text-align: center; color: #6B7280; font-size: 0.85rem; padding: 16px 0;">
    148 players · 9,970 shots · StatsBomb 2015-16 · Football Manager 2017 ratings<br>
    Visit <strong>About</strong> in the sidebar for full methodology, abstract, and research paper.
</div>
""", unsafe_allow_html=True)

# Footer
from utils.footer import render_footer
render_footer()