import streamlit as st

def render_footer():
    """Render footer pinned to bottom of page."""
    st.markdown("""
    <style>
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background: #0A0E1A;
        border-top: 1px solid rgba(59, 130, 246, 0.2);
        padding: 10px 32px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        z-index: 999;
        font-size: 0.75rem;
        color: #6B7280;
    }
    .footer a { color: #3B82F6; text-decoration: none; }
    .footer a:hover { text-decoration: underline; }
    /* Add bottom padding to page content so footer doesn't overlap */
    .main .block-container { padding-bottom: 60px !important; }
    </style>
    <div class="footer">
        <span>© 2025 What If They Took The Shot? | Mahmudlu, Karakuş & Arkadaş (2025)</span>
        <span>
            <a href="https://statsbomb.com" target="_blank">StatsBomb</a> · 
            <a href="https://www.footballmanager.com" target="_blank">FM 2017</a> · 
            <a href="https://arxiv.org/abs/2511.23072" target="_blank">📄 Read the paper</a>
        </span>
    </div>
    """, unsafe_allow_html=True)