from pathlib import Path
import librosa
import numpy as np

# audio processing and upload system

audio_path = Path(__file__).parent / 'sample.wav'

audio, original_sample_rate = librosa.load(audio_path, sr=None)

print("Audio loaded successfully")
print("Sample rate:", original_sample_rate)
print("Duration:", librosa.get_duration(y=audio, sr=original_sample_rate))

# note detection block

f0, voice_flag, voiced_probs = librosa.pyin(
    audio,
    fmin=librosa.note_to_hz("A0"),
    fmax=librosa.note_to_hz("C8")
)

times = librosa.frames_to_time(
    range(len(f0)),
    sr=original_sample_rate,
    hop_length=512
)

print("\nDetected notes:")

for i, frequency in enumerate(f0):
    if not np.isnan(frequency):
        note = librosa.hz_to_note(frequency)
        print(f"{frequency:.2f} Hz -> {note}")
# start and end
