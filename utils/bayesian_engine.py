import numpy as np

N_SAMPLES = 1000  # posterior samples for uncertainty estimation
SEED = 42


def predict_bayesian_xg(player_name, features, bayesian_data):
    """
    Point estimate: sigmoid(intercept + sum(player_coeffs * features))
    Returns single xG value.
    """
    intercept = bayesian_data["model_params"]["intercept"]
    coeffs = np.array(bayesian_data["players"][player_name]["coeffs"])
    logit = intercept + np.sum(coeffs * features)
    return float(1 / (1 + np.exp(-logit)))


def predict_bayesian_xg_with_uncertainty(player_name, features, bayesian_data):
    """
    Samples from Normal(coeffs, uncertainty) N_SAMPLES times.
    Returns (mean_xg, lower_95, upper_95, all_samples).
    """
    rng = np.random.default_rng(SEED)
    intercept = bayesian_data["model_params"]["intercept"]
    coeffs = np.array(bayesian_data["players"][player_name]["coeffs"])
    uncertainty = np.array(bayesian_data["players"][player_name]["uncertainty"])

    # Sample coefficients from posterior approximation
    sampled_coeffs = rng.normal(loc=coeffs, scale=uncertainty,
                                size=(N_SAMPLES, len(coeffs)))

    # Compute xG for each sample
    logits = intercept + np.sum(sampled_coeffs * features, axis=1)
    xg_samples = 1 / (1 + np.exp(-logits))

    mean_xg = float(np.mean(xg_samples))
    lower = float(np.percentile(xg_samples, 2.5))
    upper = float(np.percentile(xg_samples, 97.5))

    return mean_xg, lower, upper, xg_samples


def get_feature_contributions(player_name, features, bayesian_data):
    """
    Per-feature contribution to the logit.
    Returns dict of {feature_name: contribution_value}
    """
    feature_names = [
        "Distance", "GK Distance", "Angle",
        "Left Foot", "Other Body Part", "Right Foot",
        "Diving Header", "Half Volley", "Lob",
        "Normal Tech", "Overhead Kick", "Volley",
        "First Time", "One on One", "Under Pressure",
        "Penalty Area", "Defenders"
    ]
    coeffs = np.array(bayesian_data["players"][player_name]["coeffs"])
    contributions = coeffs * features

    return dict(zip(feature_names, contributions.tolist()))