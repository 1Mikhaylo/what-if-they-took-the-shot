# ⚽ What If They Took The Shot?

Interactive web application for exploring **Hierarchical Bayesian xG (expected goals)** models in football/soccer. Compare player-specific finishing abilities and run counterfactual analyses.

**Live Demo:** [whatiftheytook.streamlit.app](https://whatiftheytook.streamlit.app)
**Paper:** [arXiv:2511.23072](https://arxiv.org/abs/2511.23072)

---

## 🎯 Features

### 1. Shot Predictor
- Configure custom shot scenarios (distance, angle, body part, technique, defenders)
- Compare **Bayesian** (player-specific) vs **XGBoost** (population) xG predictions
- Interactive pitch visualization with defender positioning
- Uncertainty quantification with 95% credible intervals
- Feature contribution analysis

### 2. Player Profiles
- Finishing fingerprints (17-feature radar charts)
- Shot history from 2015-16 season
- Specialization analysis (strengths vs weaknesses)
- Comparison against global average

### 3. Counterfactual Simulator
- Answer: *"What if Player B took Player A's shots?"*
- Full posterior distribution comparison
- Shot-by-shot breakdown with xG deltas
- Uncertainty-aware analysis with credible intervals

---

## 📊 Methodology

**Hierarchical Bayesian Framework**
- Player-specific finishing coefficients
- Informed priors from Football Manager 2017 ratings
- Posterior inference from StatsBomb shot data
- Uncertainty quantification via sampling

**Baseline Comparison**
- XGBoost population-level model
- No player identity (treats all finishers equally)

**Data Sources**
- **Shot data:** [StatsBomb](https://statsbomb.com) (9,970 shots from 2015-16 season)
- **Player ratings:** Football Manager 2017
- **Leagues:** Europe's top 5 leagues

**Full methodology:** See our paper on [arXiv:2511.23072](https://arxiv.org/abs/2511.23072)

---

## 🚀 Installation

### Prerequisites
- Python 3.8+
- pip

### Setup

1. **Clone the repository**
```bash
   git clone https://github.com/yourusername/what-if-they-took-the-shot.git
   cd what-if-they-took-the-shot
```

2. **Install dependencies**
```bash
   pip install -r requirements.txt
```

3. **Run the app**
```bash
   streamlit run app.py
```

4. **Open in browser**
```
   http://localhost:8501
```

---

## 📁 Project Structure
```
FootballScouting/
├── app.py                      # Home page
├── pages/
│   ├── 1_Shot_Predictor.py
│   ├── 2_Player_Profiles.py
│   └── 3_Counterfactual.py
├── utils/
│   ├── data_loader.py          # Data loading with caching
│   ├── feature_engineering.py  # Feature vector builders
│   ├── bayesian_engine.py      # Bayesian xG predictions
│   ├── xgboost_engine.py       # XGBoost predictions
│   ├── plotly_theme.py         # Custom chart styling
│   ├── footer.py               # Reusable footer component
│   └── error_handler.py        # Error handling utilities
├── data/
│   ├── scouting_model.json     # Bayesian model parameters
│   ├── xgboost_model.pkl       # XGBoost trained model
│   ├── xg_model_input_full.csv # Shot dataset
│   └── player_id_mapping.csv   # Player metadata
├── .streamlit/
│   └── config.toml             # Dark theme configuration
└── requirements.txt
```

---

## 🎨 Tech Stack

- **Frontend:** Streamlit 1.53+
- **Data Science:** NumPy, Pandas, Scikit-learn
- **ML Models:** XGBoost 3.1+, Custom Bayesian implementation
- **Visualization:** Plotly, Matplotlib, mplsoccer
- **Styling:** Custom CSS with Exo + Roboto Mono fonts, dark analytics theme

---

## 📖 Usage Examples

### Shot Predictor
```
1. Select a player (e.g., Mohamed Salah)
2. Configure shot parameters or use quick presets:
   - Penalty
   - 1v1 Break
   - Edge of Box
   - Long Range
   - Header
   - First Touch
3. Click "CALCULATE xG"
4. Compare Bayesian vs XGBoost predictions
5. Analyze feature contributions and uncertainty
```

### Player Profiles
```
1. Select a player from the dropdown
2. View finishing fingerprint radar chart
3. Explore shot history table
4. Analyze specialization profile
```

### Counterfactual Analysis
```
1. Select Player A (shot provider, e.g., Jamie Vardy)
2. Select Player B (ability provider, e.g., Olivier Giroud)
3. Optional: Click "↔ Swap Players" to reverse
4. Click "RUN COUNTERFACTUAL ANALYSIS"
5. Review expected goals comparison and posterior distributions
6. Examine shot-by-shot breakdown
```

---

## ⚠️ Limitations

- Data limited to **2015-16 season** (players not in that season won't have predictions)
- Model trained on **Europe's top 5 leagues** only

---

## 📄 Citation

If you use this tool or methodology in research, please cite:
```bibtex
@article{mahmudlu2025whatif,
  title={What If They Took the Shot? A Hierarchical Bayesian Framework for Counterfactual Expected Goals},
  author={Mahmudlu, Mikayil and Karakuş, Oktay and Arkadaş, Hasan},
  journal={arXiv preprint arXiv:2511.23072},
  year={2025}
}
```

**Paper:** https://arxiv.org/abs/2511.23072

---

## 👥 Authors

- **Mikayil Mahmudlu** 
- **Oktay Karakuş**
- **Hasan Arkadaş**

*Research project, 2025*

---

## 📜 License

**Code:** MIT License (see LICENSE file)

**Paper:** This work is based on the research paper:
> *"What If They Took the Shot? A Hierarchical Bayesian Framework for Counterfactual Expected Goals"*  
> Mikayil Mahmudlu, Oktay Karakuş, Hasan Arkadaş (2025)  
> arXiv:2511.23072 [eess.SP]  
> Licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

**Data Attributions:**
- **StatsBomb** open data: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)
- **Football Manager** ratings: Reference only (educational use)

---

##  Acknowledgments

- **StatsBomb** for open shot data
- **Football Manager** for player ratings reference
- **Streamlit** for the web framework
- **mplsoccer** for pitch visualization tools
- **UI/UX Pro Max** design system for professional styling

---

##  Known Issues & Future Work

- Add more seasons (expand beyond 2015-16)
- Include more leagues (currently Europe top 5 only)
- Mobile optimization for smaller screens
- Export functionality (download results as CSV/PDF)

---

## 🤝 Contributing

This is a research project. For questions, issues, or collaboration inquiries:
- Open an issue on GitHub
- Contact authors via arXiv paper

---

**Built with ❤️ for football analytics research**
