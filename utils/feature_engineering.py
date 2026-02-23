import numpy as np

# ── StandardScaler parameters (fitted on training data) ──────────────────────
SCALER_PARAMS = {
    "shot_distance": {"mean": 18.644652, "std": 8.090614},
    "gk_distance":   {"mean": 3.979684,  "std": 2.721485},
    "shot_angle":    {"mean": 0.437592,  "std": 0.257901},
}

# ── LabelEncoder mappings (alphabetical — matches training) ───────────────────
BODY_PART_ENCODING = {
    "Head": 0,
    "Left Foot": 1,
    "Other": 2,
    "Right Foot": 3,
}

TECHNIQUE_ENCODING = {
    "Backheel": 0,
    "Diving Header": 1,
    "Half Volley": 2,
    "Lob": 3,
    "Normal": 4,
    "Overhead Kick": 5,
    "Volley": 6,
}

# ── UI options (for dropdowns in pages) ───────────────────────────────────────
BODY_PART_OPTIONS  = ["Head", "Left Foot", "Right Foot", "Other"]
TECHNIQUE_OPTIONS  = ["Normal", "Half Volley", "Volley", "Lob",
                      "Overhead Kick", "Diving Header", "Backheel"]


def build_bayesian_features(shot_distance, gk_distance, shot_angle,
                             body_part, technique,
                             first_time, one_on_one, under_pressure,
                             within_penalty_area, num_defenders):
    """
    Converts 10 raw inputs into 17-element feature vector for Bayesian model.
    Order must exactly match preprocessor ColumnTransformer output.
    """
    # Continuous → StandardScaled
    dist_scaled  = (shot_distance - SCALER_PARAMS["shot_distance"]["mean"]) / SCALER_PARAMS["shot_distance"]["std"]
    gk_scaled    = (gk_distance   - SCALER_PARAMS["gk_distance"]["mean"])   / SCALER_PARAMS["gk_distance"]["std"]
    angle_scaled = (shot_angle    - SCALER_PARAMS["shot_angle"]["mean"])    / SCALER_PARAMS["shot_angle"]["std"]

    # Body part → OHE (Head is reference = all zeros)
    bp_left  = 1 if body_part == "Left Foot"  else 0
    bp_other = 1 if body_part == "Other"       else 0
    bp_right = 1 if body_part == "Right Foot"  else 0

    # Technique → OHE (Backheel is reference = all zeros)
    tech_dive    = 1 if technique == "Diving Header" else 0
    tech_halfvol = 1 if technique == "Half Volley"   else 0
    tech_lob     = 1 if technique == "Lob"           else 0
    tech_normal  = 1 if technique == "Normal"        else 0
    tech_over    = 1 if technique == "Overhead Kick" else 0
    tech_volley  = 1 if technique == "Volley"        else 0

    return np.array([
        dist_scaled, gk_scaled, angle_scaled,
        bp_left, bp_other, bp_right,
        tech_dive, tech_halfvol, tech_lob, tech_normal, tech_over, tech_volley,
        int(first_time), int(one_on_one), int(under_pressure),
        int(within_penalty_area), num_defenders
    ], dtype=np.float32)


def build_xgboost_features(shot_distance, gk_distance, shot_angle,
                            body_part, technique,
                            first_time, one_on_one, under_pressure,
                            within_penalty_area, num_defenders):
    """
    Converts 10 raw inputs into 10-element feature vector for XGBoost model.
    Categoricals use LabelEncoding. No scaling applied.
    """
    return np.array([
        shot_distance,
        gk_distance,
        shot_angle,
        num_defenders,
        int(within_penalty_area),
        int(under_pressure),
        int(first_time),
        BODY_PART_ENCODING[body_part],
        TECHNIQUE_ENCODING[technique],
        int(one_on_one),
    ], dtype=np.float32)