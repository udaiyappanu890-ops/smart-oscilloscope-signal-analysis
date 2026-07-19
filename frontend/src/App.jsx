import { useEffect, useState } from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip } from 'recharts';

function App() {
  const [waveData, setWaveData] = useState([]);
  const [fftData, setFftData] = useState([]);
  const [anomaly, setAnomaly] = useState(false);

  useEffect(() => {
    const ws = new WebSocket("ws://localhost:8000/ws/live");
    ws.onmessage = (event) => {
      const data = JSON.parse(event.data);
      const wave = data.times.map((t, i) => ({ time: t.toFixed(3), value: data.samples[i] }));
      const fft = data.fft_freqs.map((f, i) => ({ freq: f.toFixed(0), mag: data.fft_mags[i] }));
      setWaveData(wave);
      setFftData(fft);
      setAnomaly(data.anomaly);
    };
    return () => ws.close();
  }, []);

  return (
    <div style={{ padding: 20, fontFamily: 'sans-serif', background: '#111', color: '#fff', minHeight: '100vh' }}>
      <h1>Smart Oscilloscope Dashboard</h1>
      {anomaly && <div style={{ background: 'red', padding: 10, marginBottom: 10 }}>⚠ Anomaly Detected!</div>}

      <h3>Time Domain</h3>
      <LineChart width={700} height={250} data={waveData}>
        <CartesianGrid stroke="#333" />
        <XAxis dataKey="time" />
        <YAxis />
        <Tooltip />
        <Line type="monotone" dataKey="value" stroke="#00ff99" dot={false} isAnimationActive={false} />
      </LineChart>

      <h3>Frequency Domain (FFT)</h3>
      <LineChart width={700} height={250} data={fftData}>
        <CartesianGrid stroke="#333" />
        <XAxis dataKey="freq" />
        <YAxis />
        <Tooltip />
        <Line type="monotone" dataKey="mag" stroke="#00aaff" dot={false} isAnimationActive={false} />
      </LineChart>
    </div>
  );
}

export default App;