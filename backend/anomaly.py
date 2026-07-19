import numpy as np
import joblib

# Load the trained model once when the app starts
model = joblib.load("anomaly_model.pkl")

def extract_features(signal):
    signal = np.array(signal)
    peak = np.max(np.abs(signal))
    rms = np.sqrt(np.mean(signal**2))
    std = np.std(signal)
    mean = np.mean(signal)
    return [peak, rms, std, mean]

def detect_anomaly(signal, threshold=3.0):
    features = extract_features(signal)
    prediction = model.predict([features])  # returns -1 for anomaly, 1 for normal
    return bool(prediction[0] == -1)