import librosa
import matplotlib.pyplot as plt
import numpy as np

y, sr = librosa.load("audio.mp3")

# Normalize to [-1,1]
y = y / np.max(np.abs(y))

plt.figure(figsize=(12, 6))
plt.plot(y, linewidth=0.8)
plt.title("Waveform")
plt.xlabel("Sample")
plt.ylabel("Amplitude")
plt.ylim(-1.1, 1.1)
plt.tight_layout()
plt.show()

def plot_zoom(y, sr, start_sec, end_sec):
    start = int(start_sec * sr)
    end = int(end_sec * sr)

    plt.figure(figsize=(12, 4))

    # x 轴换成秒，更直观
    time_axis = np.linspace(start_sec, end_sec, end - start)

    plt.plot(time_axis, y[start:end])
    plt.title(f"Waveform ({start_sec}s to {end_sec}s)")
    plt.xlabel("Time (seconds)")
    plt.ylabel("Amplitude")
    plt.tight_layout()
    plt.show()

plot_zoom(y, sr, 0, 0.5)
plot_zoom(y, sr, 1, 1.5)
plot_zoom(y, sr, 2, 2.5)