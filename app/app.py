# app/app.py
from flask import Flask, request, jsonify
import joblib
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)

# Models load karo
rf = joblib.load('../models/random_forest_ids.pkl')
scaler = joblib.load('../models/scaler.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        
        input_df = pd.DataFrame([data])
        
        # Categorical encode
        cat_cols = ['protocol_type', 'service', 'flag']
        le = LabelEncoder()
        for col in cat_cols:
            input_df[col] = le.fit_transform(
                input_df[col].astype(str)
            )
        
        scaled = scaler.transform(input_df)
        pred = rf.predict(scaled)[0]
        prob = rf.predict_proba(scaled)[0]
        
        return jsonify({
            "prediction": "ATTACK" if pred == 1 else "NORMAL",
            "confidence": f"{max(prob)*100:.2f}%",
            "attack_probability": f"{prob[1]*100:.2f}%"
        })
    
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "IDS API running ✅"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)