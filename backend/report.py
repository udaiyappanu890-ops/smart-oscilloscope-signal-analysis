import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
import os
import time

def generate_report(session_log):
    os.makedirs("reports", exist_ok=True)
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    waveform_img = f"reports/waveform_{timestamp}.png"
    fft_img = f"reports/fft_{timestamp}.png"
    pdf_path = f"reports/report_{timestamp}.pdf"

    plt.figure(figsize=(6, 3))
    plt.plot(session_log["times"], session_log["samples"], color="green")
    plt.title("Time Domain Signal")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.tight_layout()
    plt.savefig(waveform_img)
    plt.close()

    plt.figure(figsize=(6, 3))
    plt.plot(session_log["fft_freqs"], session_log["fft_mags"], color="blue")
    plt.title("Frequency Spectrum (FFT)")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude")
    plt.tight_layout()
    plt.savefig(fft_img)
    plt.close()

    c = canvas.Canvas(pdf_path, pagesize=A4)
    width, height = A4

    c.setFont("Helvetica-Bold", 16)
    c.drawString(1 * inch, height - 1 * inch, "Smart Oscilloscope - Diagnostic Report")

    c.setFont("Helvetica", 11)
    c.drawString(1 * inch, height - 1.4 * inch, f"Generated: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    c.drawString(1 * inch, height - 1.7 * inch, f"Total Anomalies Detected: {session_log['anomaly_count']}")

    if session_log["anomaly_timestamps"]:
        ts_text = ", ".join(session_log["anomaly_timestamps"][-5:])
        c.drawString(1 * inch, height - 2.0 * inch, f"Recent Anomaly Times: {ts_text}")

    c.drawImage(waveform_img, 1 * inch, height - 5 * inch, width=5.5 * inch, height=2.5 * inch)
    c.drawImage(fft_img, 1 * inch, height - 7.5 * inch, width=5.5 * inch, height=2.5 * inch)

    c.save()
    return pdf_path