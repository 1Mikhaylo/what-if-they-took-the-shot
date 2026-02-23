import json
import joblib
import pandas as pd
import streamlit as st

DATA_DIR = "data/"

@st.cache_data
def load_bayesian_data():
    with open(DATA_DIR + "scouting_model.json", "r") as f:
        return json.load(f)

@st.cache_data
def load_player_mapping():
    return pd.read_csv(DATA_DIR + "player_id_mapping.csv")

@st.cache_data
def load_shots_data():
    return pd.read_csv(DATA_DIR + "xg_model_input_full.csv")

@st.cache_resource
def load_xgboost_model():
    return joblib.load(DATA_DIR + "xgboost_model.pkl")

@st.cache_data
def load_preferred_foot():
    """Load player preferred foot data."""
    df = pd.read_csv(DATA_DIR + "player_preferred_foot.csv")
    # Create dictionary for fast lookup: {player_name: preferred_foot}
    return dict(zip(df['player_name'], df['preferred_foot']))