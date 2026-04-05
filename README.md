# 🛡️ AI-Powered Network Intrusion Detection System

> A machine learning pipeline that detects network intrusions in real-time using ensemble methods — validated across two datasets and deployable as a REST API.

---

## 📊 Results at a Glance

| Dataset | Model | Accuracy | Notes |
|---|---|---|---|
| KDD Cup 99 | Random Forest | **99.98%** | Classic benchmark |
| KDD Cup 99 | XGBoost | **99.98%** | Classic benchmark |
| UNSW-NB15 | Random Forest | **~90%** | Modern attacks |

> ⚠️ High accuracy on KDD99 is expected and well-documented in literature — the dataset is intentionally structured for classification benchmarking. Cross-validation on UNSW-NB15 confirms the model generalises beyond the training distribution.

---

## 🧠 How It Works

```
Raw Network Traffic (41 features)
        ↓
Label Encoding  →  Categorical → Numeric (protocol, service, flag)
        ↓
StandardScaler  →  Normalise all features to same scale
        ↓
Train/Test Split  →  80% train / 20% test (stratified)
        ↓
┌─────────────────┐     ┌──────────────┐
│  Random Forest  │     │   XGBoost    │
│  100 trees      │     │  Sequential  │
│  Majority vote  │     │  boosting    │
└─────────────────┘     └──────────────┘
        ↓
  Binary Classification: NORMAL ✅  or  ATTACK 🚨
        ↓
  Flask REST API  →  Real-time predictions
```

---

## 🔍 Top Discriminating Features

| Feature | Why It Matters |
|---|---|
| `count` | Spike in connections to same host = DDoS indicator |
| `dst_bytes` | Unusually high received bytes = data exfiltration |
| `logged_in` | Unauthenticated connections = brute force / probe |
| `src_bytes` | High outgoing bytes = flood attack |
| `protocol_type` | ICMP-heavy traffic = ping flood (Smurf attack) |

---

## 🚀 Quick Start

### 1. Clone & Install
```bash
git clone https://github.com/YOUR_USERNAME/AI-Intrusion-Detection.git
cd AI-Intrusion-Detection
pip install -r requirements.txt
```

### 2. Run the Notebook
```bash
jupyter notebook notebooks/IDS_Model.ipynb
```

### 3. Start the API
```bash
cd app
python app.py
```

### 4. Test the API
```bash
python test_api.py
```

**Sample Response:**
```json
{
  "prediction": "✅ NORMAL",
  "confidence": "99.87%",
  "attack_probability": "0.13%"
}
```

---

## 📁 Project Structure

```
AI-Intrusion-Detection/
├── app/
│   ├── app.py                  ← Flask REST API
│   └── test_api.py             ← API test script
├── notebooks/
│   ├── IDS_Model.ipynb         ← Full ML pipeline
│   └── IDS_Model.html          ← Static results viewer
├── models/
│   ├── accuracy_comparison.png
│   ├── confusion_matrix.png
│   ├── feature_importance.png
│   ├── roc_curve.png
│   └── kdd_vs_unsw.png
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🌍 Real-World Applications

| Use Case | How This Applies |
|---|---|
| **University/Office Network Monitor** | Deploy API on gateway server — flag suspicious connections live |
| **Edge Security (Raspberry Pi)** | Lightweight `.pkl` model (~50MB) runs on RPi for IoT network monitoring |
| **SDR Signal Anomaly Detection** | Same classification pipeline — swap network features for radio signal features |
| **SOC Automation** | API integrates with SIEM tools to auto-triage alerts |

---

## 🔬 Cross-Dataset Validation

The model was additionally evaluated on **UNSW-NB15** — a modern dataset containing attacks that did not exist when KDD99 was created (2019 vs 1999).

- KDD99 → UNSW-NB15 direct transfer: ❌ (only 1 common feature — `service`)
- Fresh model trained on UNSW-NB15: ✅ ~90% accuracy
- This confirms the pipeline architecture generalises — not just the weights

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.3-orange)
![XGBoost](https://img.shields.io/badge/XGBoost-2.0-green)
![Flask](https://img.shields.io/badge/Flask-3.0-lightgrey)

- **ML:** Scikit-learn, XGBoost, Imbalanced-learn
- **Data:** Pandas, NumPy
- **Viz:** Matplotlib, Seaborn
- **API:** Flask
- **Persistence:** Joblib

---

## 📚 Datasets

- [KDD Cup 1999](http://kdd.ics.uci.edu/databases/kddcup99/kddcup99.html) — via `sklearn.datasets.fetch_kddcup99`
- [UNSW-NB15](https://research.unsw.edu.au/projects/unsw-nb15-dataset) — University of New South Wales, 2015

---

## 👤 Author

**Your Name**  
B.Eng. CSE (Honors in Cybersecurity) — Chandigarh University  
[GitHub](https://github.com/YOUR_USERNAME) · [LinkedIn](https://linkedin.com/in/YOUR_PROFILE)
