
"""
Configuration file for Bayesian Scout Pro
Stores all constants and settings in one place
"""

# ============================================
# MODEL PATHS
# ============================================
BAYESIAN_MODEL_PATH = "data/scouting_model.json"
XGBOOST_MODEL_PATH = "data/xgboost_model.pkl"

# ============================================
# STANDARDIZATION PARAMETERS
# ============================================
# These values are used to standardize continuous features
# Formula: (value - mean) / std

# ============================================
# STANDARDIZATION PARAMETERS (FROM TRAINING)
# ============================================

# Distance to goal (meters)
DISTANCE_MEAN = 18.644651941807286
DISTANCE_STD = 8.090614391388657

# Goalkeeper distance (meters)
GK_DISTANCE_MEAN = 3.9796840096025217
GK_DISTANCE_STD = 2.72148457151183

# Shot angle (radians)
ANGLE_MEAN = 0.4375916000980637
ANGLE_STD = 0.2579010152191712

# ============================================
# FEATURE MAPPINGS
# ============================================

# Body part options for user selection
BODY_PART_OPTIONS = ["Left Foot", "Right Foot", "Head/Other"]

# Technique options for user selection
TECHNIQUE_OPTIONS = [
    "Normal",
    "Volley", 
    "Half Volley",
    "Diving Header",
    "Lob",
    "Overhead Kick"
]

# ============================================
# LABEL ENCODER MAPPINGS (XGBoost)
# ============================================
# XGBoost uses label encoding (alphabetical order)

# Body Part: alphabetically sorted
BODY_PART_LABEL_MAP = {
    "Head/Other": 0,      # 'H' comes first
    "Left Foot": 1,       # 'L' comes second
    "Right Foot": 2       # 'R' comes last
}

# Technique: alphabetically sorted
TECHNIQUE_LABEL_MAP = {
    "Diving Header": 0,
    "Half Volley": 1,
    "Lob": 2,
    "Normal": 3,
    "Overhead Kick": 4,
    "Volley": 5
}

# ============================================
# UI SETTINGS
# ============================================
APP_TITLE = "⚽ Bayesian Scout Pro"
APP_SUBTITLE = "Dual-Engine xG Prediction System"
PAGE_ICON = "⚽"

# Color scheme
PRIMARY_COLOR = "#00FF87"      # Football green
SECONDARY_COLOR = "#4A90E2"    # Blue
BACKGROUND_COLOR = "#0A0E27"   # Dark navy

# ============================================
# PITCH SETTINGS
# ============================================
# StatsBomb pitch dimensions
PITCH_LENGTH = 120
PITCH_WIDTH = 80
GOAL_Y_CENTER = 40

# Default shot position
DEFAULT_X = 100
DEFAULT_Y = 40