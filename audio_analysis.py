import librosa
audio_path = "piano.wav"

audio, original_sample_rate = librosa.load(audio_path, sr=None)
print("Audio loaded successfully")
print("Sample rate:", original_sample_rate)
print("Duration:", librosa.get_duration(y=audio, sr=original_sample_rate))
