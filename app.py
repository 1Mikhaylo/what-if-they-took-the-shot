import streamlit as st

st.set_page_config(
    page_title="What If They Took The Shot?",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Global fonts and styling
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Exo:wght@300;400;500;600;700&family=Roboto+Mono:wght@300;400;500;700&display=swap');

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
</style>
""", unsafe_allow_html=True)

# Logo + Title
st.markdown("""
<div style="display: flex; align-items: center; gap: 16px; margin-bottom: 24px;">
    <div style="
        width: 56px; 
        height: 56px; 
        background: linear-gradient(135deg, #3B82F6, #10B981);
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 28px;
        font-weight: 700;
        color: white;
        box-shadow: 0 4px 12px rgba(59, 130, 246, 0.3);
    ">W</div>
    <h1 style="margin: 0; font-size: 2.5rem; font-weight: 700; color: #F9FAFB;">
        What If They Took The Shot?
    </h1>
</div>
""", unsafe_allow_html=True)

st.markdown("### Hierarchical Bayesian xG — Player-Specific Finishing Analysis")
st.markdown("*Mahmudlu, Karakuş & Arkadaş (2025)*")
st.markdown("---")

st.markdown("""
An interactive research tool exploring **player-specific expected goals (xG)** using hierarchical Bayesian modeling.

**Standard xG models treat all players equally.** This app shows how individual finishing ability affects shot outcomes.
""")

st.info("👈 **Use the sidebar** to navigate. Visit **About** for full methodology and research paper.")

# Footer
from utils.footer import render_footer
render_footer()