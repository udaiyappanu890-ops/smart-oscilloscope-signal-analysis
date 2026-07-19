from signal_generator import SignalGenerator
from dsp import compute_fft

gen = SignalGenerator()
samples, _ = gen.generate_window(freq=50)
freqs, mags = compute_fft(samples, 1000)

print("Frequencies:", freqs[:5])
print("Magnitudes:", mags[:5])

peak_index = mags.index(max(mags))
print("Peak Frequency Detected:", freqs[peak_index], "Hz")