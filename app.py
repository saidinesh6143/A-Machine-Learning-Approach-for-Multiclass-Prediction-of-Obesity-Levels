from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load model and encoders
model = joblib.load('xgboost_model.pkl')
encoders = joblib.load('label_encoders.pkl')

# Feature columns
features = ['Gender', 'Age', 'Height', 'Weight', 'family_history_with_overweight',
            'FAVC', 'FCVC', 'NCP', 'CAEC', 'SMOKE', 'CH2O', 'SCC',
            'FAF', 'TUE', 'CALC', 'MTRANS']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        input_data = []
        for feat in features:
            val = request.form[feat]
            if feat in encoders:
                val = encoders[feat].transform([val])[0]
            else:
                val = float(val)
            input_data.append(val)

        prediction = model.predict([input_data])[0]
        output = encoders['NObeyesdad'].inverse_transform([prediction])[0]
        return render_template('index.html', prediction_text=f"Predicted Obesity Level: {output}")
    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {e}")

if __name__ == '__main__':
    app.run(debug=True)
