from pathlib import Path
import librosa
import numpy as np

# audio processing and upload functionality

audio_path = Path(__file__).parent / 'sample.wav'

audio, original_sample_rate = librosa.load(audio_path, sr=None)

print("Audio loaded successfully")
print("Sample rate:", original_sample_rate)
print("Duration:", librosa.get_duration(y=audio, sr=original_sample_rate))

# note detection block

f0, voice_flag, voiced_probs = librosa.pyin(  # f0: the frequency of a specific note
    audio,
    fmin=librosa.note_to_hz("A0"),
    fmax=librosa.note_to_hz("C8")
)
# create timestamps for each note
times = librosa.frames_to_time(
    range(len(f0)),
    sr=original_sample_rate,
    hop_length=512  # hop_length: number of samples between successive frames
)

print("\nDetected notes:")

start_time = None
end_time = None
notes = []
current_note = None

# Converting the base frequency to actual notes
for i, frequency in enumerate(f0):
    if not np.isnan(frequency):
        note = librosa.hz_to_note(frequency)
        print(f"{frequency:.2f} Hz -> {note}")

    elif current_note == None:
        current_note = note
        start_time = times[i]

    elif note == current_note:
        continue

    else:
        end_time = times[i]

        notes.append({
            "note": current_note,
            "start": start_time,
            "end": end_time
        })

        current_note = note  # current note changes from one to the next
        start_time = times[i]

    if np.isnan(frequency):
        current_note = None
        start_time = times[i]

    elif current_note == None:
        continue

    else:
        end_time = times[i]

        notes.append({
            "note": current_note,
            "start": start_time,
            "end": end_time
        })
        current_note = note
        start_time = [i]
