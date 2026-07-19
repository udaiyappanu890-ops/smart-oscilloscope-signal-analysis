import numpy as np
import time

class SignalGenerator:
    def __init__(self, sample_rate=1000):
        self.sample_rate = sample_rate
        self.t = 0

    def generate_window(self, window_size=256, freq=50, noise_level=0.05, inject_anomaly=False):
        t_vals = np.arange(self.t, self.t + window_size) / self.sample_rate
        signal = np.sin(2 * np.pi * freq * t_vals)
        signal += np.random.normal(0, noise_level, window_size)

        if inject_anomaly:
            spike_idx = np.random.randint(0, window_size)
            signal[spike_idx] += np.random.uniform(2, 4)

        self.t += window_size
        return signal.tolist(), t_vals.tolist()

if __name__ == "__main__":
    gen = SignalGenerator()
    samples, times = gen.generate_window()
    print(samples[:10])
    