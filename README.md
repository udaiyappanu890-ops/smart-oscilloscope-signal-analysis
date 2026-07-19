# Smart Oscilloscope & Signal Analysis Platform

A full-stack signal analysis system that combines embedded signal acquisition, real-time DSP (FFT), machine learning-based anomaly detection, and a live web dashboard.

## Overview

This project simulates a smart, AI-assisted oscilloscope. Signal data is generated (with support for real ESP32-based ADC acquisition), analyzed in real time using FFT-based spectral analysis, and monitored using a trained Isolation Forest model to detect anomalies such as noise spikes and glitches. Everything is visualized live in a web dashboard, with automated PDF diagnostic report generation.

## Features

- Real-time signal streaming via WebSocket (FastAPI backend to React frontend)
- FFT-based spectral analysis using SciPy
- ML-based anomaly detection using scikit-learn's Isolation Forest
- Live web dashboard built with React and Recharts
- Automated PDF report generation with waveform and FFT snapshots
- Embedded firmware (ESP32) with real ADC sampling code, simulated using Wokwi

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
# React + Vite

This template provides a minimal setup to get React working in Vite with HMR and some ESLint rules.