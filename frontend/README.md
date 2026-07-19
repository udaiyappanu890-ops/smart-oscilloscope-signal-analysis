# Smart Oscilloscope & Signal Analysis Platform

A full-stack signal analysis system that combines embedded signal acquisition, real-time DSP (FFT), machine learning-based anomaly detection, and a live web dashboard — inspired by real oscilloscope diagnostic tools.

## Overview

This project simulates a smart, AI-assisted oscilloscope. Signal data is generated (with support for real ESP32-based ADC acquisition), analyzed in real time using FFT-based spectral analysis, and monitored using a trained Isolation Forest model to detect anomalies such as noise spikes and glitches. All of this is visualized live in a web dashboard, with automated PDF diagnostic report generation.

## Features

- **Real-time signal streaming** via WebSocket (FastAPI backend → React frontend)
- **FFT-based spectral analysis** using SciPy — time domain and frequency domain visualization
- **ML-based anomaly detection** using scikit-learn's Isolation Forest, trained on normal signal patterns
- **Live web dashboard** built with React and Recharts, showing waveform + FFT + real-time anomaly alerts
- **Automated PDF report generation** — waveform snapshots, FFT spectrum, and anomaly summary
- **Embedded firmware (ESP32)** — real ADC sampling code, simulated using Wokwi (no physical hardware required)

## Architecture

## Tech Stack

| Layer | Technology |
|---|---|
| Embedded | ESP32 (C++/Arduino), simulated via Wokwi |
| Backend | Python, FastAPI, WebSockets |
| DSP | NumPy, SciPy (FFT) |
| Machine Learning | scikit-learn (Isolation Forest) |
| Frontend | React, Recharts |
| Reports | Matplotlib, ReportLab |

## Setup Instructions

### Backend
```bash
cd backend
python -m venv venv
venv\Scripts\activate      # Windows
pip install fastapi uvicorn numpy scipy scikit-learn websockets python-multipart matplotlib reportlab
python train_model.py      # trains the anomaly detection model
uvicorn main:app --reload --port 8000
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

Open `http://localhost:5173` in your browser to view the live dashboard.

### Generate a Report
While the dashboard is running, visit:

### Embedded Firmware (Wokwi Simulation)
The ESP32 firmware code (ADC sampling logic) is available in the `firmware/` folder. It can be run using [Wokwi](https://wokwi.com) — no physical hardware required.

## Future Improvements

- Multi-channel signal comparison
- Real hardware integration (physical ESP32 + ADC)
- Signal classification (PWM, sine, square wave detection)
- WiFi-based direct ESP32-to-backend streaming

## Author

Built by Udaiyappan as a personal project combining embedded systems, DSP, machine learning, and full-stack development.