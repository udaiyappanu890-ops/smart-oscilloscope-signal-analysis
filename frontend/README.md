# Smart Oscilloscope & Signal Analysis Platform

A full-stack, AI-powered signal analysis platform that combines embedded signal acquisition, real-time DSP (FFT), machine learning-based anomaly detection, and a live web dashboard — with automated PDF diagnostic reporting.

## 🎯 Overview

This project simulates a smart oscilloscope system: signals are generated (simulating real ADC acquisition from an ESP32), analyzed in real time using FFT-based spectral analysis, and monitored for anomalies using a trained Isolation Forest ML model. All of this is streamed live to a React dashboard via WebSockets, with the ability to generate on-demand PDF diagnostic reports.

## ✨ Features

- **Real-time signal streaming** via WebSockets (FastAPI backend → React frontend)
- **FFT-based spectral analysis** for frequency-domain signal inspection
- **ML-based anomaly detection** using a trained Isolation Forest model (scikit-learn)
- **Live dashboard** with time-domain and frequency-domain visualizations (Recharts)
- **Automated PDF report generation** with waveform snapshots, FFT plots, and anomaly logs
- **Embedded firmware** (ESP32, C++) for real ADC signal acquisition — simulated via Wokwi

## 🏗️ Architecture

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Embedded | ESP32, C++ (Arduino framework), simulated via Wokwi |
| Backend | Python, FastAPI, WebSockets |
| DSP | NumPy, SciPy (FFT) |
| Machine Learning | scikit-learn (Isolation Forest) |
| Frontend | React, Recharts |
| Reporting | Matplotlib, ReportLab |

## 🚀 Getting Started

### Backend
```bash
cd backend
python -m venv venv
venv\Scripts\activate          # Windows
pip install -r requirements.txt
python train_model.py          # trains the anomaly detection model
uvicorn main:app --reload --port 8000
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```
Open `http://localhost:5173` in your browser.

### Embedded Firmware
Firmware code is in `/firmware`. Open in [Wokwi](https://wokwi.com) or flash directly to a real ESP32 board.

## 📊 Demo

*(Add your demo GIF/video here)*

## 📄 Sample Report

Click "Generate Report" on the dashboard, or visit `http://localhost:8000/report` while the dashboard is streaming live data.

## 🔮 Future Improvements

- Multi-channel signal comparison
- Signal type classification (PWM, sine, square, etc.)
- Real hardware deployment with live sensor integration
- Cloud-based data logging and historical trend analysis

## 👤 Author

Built by [S.Udaiyappan] as a personal project exploring embedded systems, DSP, and applied machine learning.