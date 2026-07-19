from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import asyncio
import json
import time

from signal_generator import SignalGenerator
from dsp import compute_fft
from anomaly import detect_anomaly
from report import generate_report

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

gen = SignalGenerator()

session_log = {
    "samples": [],
    "times": [],
    "fft_freqs": [],
    "fft_mags": [],
    "anomaly_count": 0,
    "anomaly_timestamps": []
}

@app.websocket("/ws/live")
async def live_stream(websocket: WebSocket):
    await websocket.accept()
    counter = 0
    try:
        while True:
            counter += 1
            inject = (counter % 15 == 0)
            samples, times = gen.generate_window(inject_anomaly=inject)
            freqs, mags = compute_fft(samples, gen.sample_rate)
            anomaly = detect_anomaly(samples)

            session_log["samples"] = samples
            session_log["times"] = times
            session_log["fft_freqs"] = freqs[:50]
            session_log["fft_mags"] = mags[:50]

            if anomaly:
                session_log["anomaly_count"] += 1
                session_log["anomaly_timestamps"].append(time.strftime("%H:%M:%S"))

            payload = {
                "samples": samples,
                "times": times,
                "fft_freqs": freqs[:50],
                "fft_mags": mags[:50],
                "anomaly": anomaly
            }
            await websocket.send_text(json.dumps(payload))
            await asyncio.sleep(0.3)
    except Exception as e:
        print("Connection closed:", e)

@app.get("/report")
def get_report():
    filepath = generate_report(session_log)
    return FileResponse(filepath, media_type="application/pdf", filename="oscilloscope_report.pdf")