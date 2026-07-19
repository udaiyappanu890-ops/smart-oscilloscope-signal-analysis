import numpy as np
from scipy.fft import fft, fftfreq

def compute_fft(signal, sample_rate):
    n = len(signal)
    yf = fft(signal)
    xf = fftfreq(n, 1 / sample_rate)[:n // 2]
    magnitude = np.abs(yf[:n // 2])
    return xf.tolist(), magnitude.tolist()