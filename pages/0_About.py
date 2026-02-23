import streamlit as st

st.set_page_config(page_title="About", page_icon="📖", layout="wide")

# Logo + Title (from app.py)
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

# Abstract
st.header("📄 Abstract")
st.markdown("""
Standard expected goals (xG) models treat all players as identical finishers—a striker and a midfielder 
receive the same xG for the same shot. This study develops a **hierarchical Bayesian framework** that 
integrates Football Manager ratings to quantify **player-specific finishing abilities**.

Using 9,970 shots from StatsBomb's 2015-16 data and Football Manager 2017 ratings, we combine Bayesian 
logistic regression with informed priors to stabilize player-level estimates, especially for players with few shots.

**Key Findings:**
- Model achieves strong external validity: hierarchical and baseline predictions correlate at R² = 0.75
- XGBoost benchmark validated against StatsBomb xG reaches R² = 0.833
- Uncovers interpretable specialization profiles (one-on-one finishing, long-range shooting, first-touch execution)
- Identifies underrated players (Immobile, Belotti) and overrated players (Agüero, Suárez)
- Case studies: Sansone would generate +2.2 xG from Berardi's chances; Vardy-Giroud substitutions reveal strong asymmetry

This work provides an **uncertainty-aware tool** for player evaluation, recruitment, and tactical planning.
""")

st.markdown("---")

# How It Works
st.header("⚙️ How It Works")

col1, col2 = st.columns(2)

with col1:
    st.subheader("🔵 Bayesian Hierarchical Model")
    st.markdown("""
    **Player-specific predictions**
    
    - 17 unique coefficients per player
    - Learned from StatsBomb shot data (9,970 shots)
    - Informed priors from Football Manager 2017 ratings
    - Captures individual strengths/weaknesses
    - Provides uncertainty estimates (95% credible intervals)
    
    **Example:** Agüero excels at one-on-one situations.  
    Pogba excels at long-range shots.
    """)

with col2:
    st.subheader("🟠 XGBoost Baseline")
    st.markdown("""
    **Population-level predictions**
    
    - Trained on shot characteristics only (10 features)
    - No player identity included
    - Represents "average finisher" benchmark
    - Industry-standard machine learning approach
    - Validated against StatsBomb xG (R² = 0.833)
    
    **Example:** All players get the same xG  
    for a 15m shot with 2 defenders.
    """)

st.markdown("---")

# Navigate the App
st.header(" Navigate The App")

st.markdown("""
Use the **sidebar** to explore three interactive tools:
""")

col3, col4, col5 = st.columns(3)

with col3:
    st.markdown("""
    **⚽ Shot Predictor**
    
    Build custom shot scenarios or use quick presets:
    - Penalty
    - 1v1 Break
    - Edge of Box
    - Long Range
    - Header
    - First Touch
    
    Compare Bayesian vs XGBoost predictions for any player.
    """)

with col4:
    st.markdown("""
    **👤 Player Profiles**
    
    Explore individual finishing fingerprints:
    - 17-feature radar charts
    - Shot history from 2015-16
    - Specialization analysis
    - Strengths vs weaknesses
    - Comparison to global average
    """)

with col5:
    st.markdown("""
    **🔄 Counterfactual Simulator**
    
    Answer "what if" questions:
    - What if Salah took Kane's shots?
    - What if Pogba played as striker?
    - Posterior distribution comparisons
    - Shot-by-shot breakdown
    - Uncertainty-aware analysis
    """)

st.markdown("---")

# Data & Limitations
st.header("📊 Data & Limitations")

st.markdown("""
**Data Sources:**
- **Shot Data:** StatsBomb open data (9,970 shots)
- **Season:** 2015-16 across Europe's top 5 leagues
- **Players:** 148 players with sufficient shot history
- **Player Ratings:** Football Manager 2017

**Limitations:**
- ⚠️ Limited to 2015-16 season with 148 players only
- ⚠️ Model trained on European top 5 leagues (EPL, La Liga, Serie A, Bundesliga, Ligue 1)
""")

st.markdown("---")

# Research Paper
st.header("📄 Research Paper")

st.markdown("""
**Title:** *What If They Took the Shot? A Hierarchical Bayesian Framework for Counterfactual Expected Goals*

**Authors:** Mikayil Mahmudlu, Oktay Karakuş, Hasan Arkadaş (2025)

**Published:** arXiv:2511.23072 [eess.SP]

**License:** CC BY 4.0

**Read the paper:** [https://arxiv.org/abs/2511.23072](https://arxiv.org/abs/2511.23072)

**Citation:**
```bibtex
@article{mahmudlu2025whatif,
  title={What If They Took the Shot? A Hierarchical Bayesian Framework for Counterfactual Expected Goals},
  author={Mahmudlu, Mikayil and Karakuş, Oktay and Arkadaş, Hasan},
  journal={arXiv preprint arXiv:2511.23072},
  year={2025}
}
```
""")

st.markdown("---")

# Tech Stack
st.header("🛠️ Tech Stack")

col6, col7 = st.columns(2)

with col6:
    st.markdown("""
    **Frontend:**
    - Streamlit 1.53+
    - Plotly for interactive charts
    - mplsoccer for pitch visualization
    - Custom CSS (Exo + Roboto Mono fonts)
    - Dark analytics theme
    """)

with col7:
    st.markdown("""
    **Backend:**
    - Python 3.8+
    - NumPy, Pandas for data processing
    - XGBoost 3.1+ for baseline model
    - Custom Bayesian implementation
    - Hierarchical modeling with informed priors
    """)

st.markdown("---")

# Footer
from utils.footer import render_footer
render_footer()