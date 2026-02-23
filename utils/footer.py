import streamlit as st

def render_footer():
    """Render footer with data credits and author info."""
    st.markdown("---")
    
    # Three columns for footer
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("#### Data Sources")
        st.markdown("""
        Shot data: [StatsBomb](https://statsbomb.com)  
        Player ratings: [Football Manager 2017](https://www.footballmanager.com)  
        Analysis period: 2015-16 season
        """)
    
    with col2:
        st.markdown("#### Methodology")
        st.markdown("""
        Hierarchical Bayesian xG model with  
        player-specific finishing coefficients.  
        Comparison baseline: XGBoost population model.
        """)
    
    with col3:
        st.markdown("""
        Mahmudlu, Karakuş & Arkadaş (2025)  
        Built with Streamlit + Python  
        [📄 Read the paper](https://arxiv.org/abs/2511.23072)
        """)
    
    # Copyright
    st.markdown("---")
    st.markdown(
        "<p style='text-align: center; color: #6B7280; font-size: 0.75rem;'>© 2025 What If They Took The Shot? | Research tool for educational purposes</p>",
        unsafe_allow_html=True
    )