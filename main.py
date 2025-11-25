from audio_io import load_audio, plot_waveform, plot_zoom

def main():
    file_path = "/Users/cccc/Desktop/Lukas Graham - 7 Years [mqms2].mp3"

    y, sr = load_audio(file_path)

    # 画全局波形
    plot_waveform(y, sr)

    # 画前 5 秒 zoom-in 波形
    plot_zoom(y, sr, 10,10.3)

if __name__ == "__main__":
    main()