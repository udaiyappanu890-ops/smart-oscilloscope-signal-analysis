import numpy as np
from sklearn.ensemble import IsolationForest
import joblib
from signal_generator import SignalGenerator

def extract_features(signal):
    signal = np.array(signal)
    peak = np.max(np.abs(signal))
    rms = np.sqrt(np.mean(signal**2))
    std = np.std(signal)
    mean = np.mean(signal)
    return [peak, rms, std, mean]

gen = SignalGenerator()
training_data = []

for _ in range(200):
    samples, _ = gen.generate_window(inject_anomaly=False)
    training_data.append(extract_features(samples))

training_data = np.array(training_data)

model = IsolationForest(contamination=0.05, random_state=42)
model.fit(training_data)

joblib.dump(model, "anomaly_model.pkl")
print("Model trained and saved as anomaly_model.pkl")