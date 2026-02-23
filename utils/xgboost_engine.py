import pandas as pd


def predict_xgboost_xg(model, features):
    """
    XGBoost prediction from 10-element feature vector.
    Returns single xG probability.
    """
    feature_names = [
        'shot_distance', 'gk_distance', 'shot_angle',
        'num_defenders_in_triangle', 'within_penalty_area',
        'under_pressure', 'shot_first_time',
        'shot_body_part', 'shot_technique', 'shot_one_on_one'
    ]
    X = pd.DataFrame([features], columns=feature_names)
    return float(model.predict_proba(X)[0][1])