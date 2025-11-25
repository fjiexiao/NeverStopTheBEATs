import matplotlib.pyplot as plt
import numpy as np
import librosa

def load_audio(file_path):
    y, sr = librosa.load(file_path, sr=None)
    y = y / np.max(np.abs(y))   # normalize
    return y, sr

def plot_waveform(y, sr):
    plt.figure(figsize=(12, 4))
    time_axis = np.linspace(0, len(y) / sr, len(y))
    plt.plot(time_axis, y, linewidth=0.8)
    plt.title("Waveform")
    plt.xlabel("Time (seconds)")
    plt.ylabel("Amplitude")
    plt.tight_layout()
    plt.show()

def plot_zoom(y, sr, start_sec, end_sec):
    start = int(start_sec * sr)
    end = int(end_sec * sr)

    plt.figure(figsize=(12, 4))
    time_axis = np.linspace(start_sec, end_sec, end - start)
    plt.plot(time_axis, y[start:end])
    plt.title(f"Waveform ({start_sec}s to {end_sec}s)")
    plt.xlabel("Time (seconds)")
    plt.ylabel("Amplitude")
    plt.tight_layout()
    plt.show()