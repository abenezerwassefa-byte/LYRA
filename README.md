# 🎵 LYRA

**LYRA** is a music transcription project that analyzes piano audio and converts detected pitches into structured musical note data.

> **Current focus:** Audio analysis and basic monophonic note detection

## 🎯 Overview

LYRA is currently **monophonic**, meaning it is designed to detect one primary note at a time rather than multiple simultaneously played notes.

---

## 🔄 Current Pipeline

```text
Audio File
    ↓
Audio Loading
    ↓
Fundamental Frequency Detection
    ↓
Frequency → Musical Note
    ↓
Basic Note Segmentation
    ↓
Structured Note Data
```

---

## ✅ Implemented

### 🎧 Audio Loading

LYRA currently loads an audio file using **Librosa** while preserving its original sample rate.

The program also calculates basic information such as:

* Sample rate
* Audio duration

### 🎵 Fundamental Frequency Detection

LYRA uses `librosa.pyin()` to estimate the fundamental frequency of the audio over time.

The current frequency range is approximately:

```text
A0 → C8
```

### ⏱️ Time Mapping

Detected pitch frames are mapped to timestamps so that notes can be associated with their approximate position in the audio.

### 🎼 Frequency-to-Note Conversion

Detected frequencies are converted into musical note names using Librosa's frequency-to-note functionality.

For example:

```text
440 Hz → A4
```

### 📝 Basic Note Segmentation

The current implementation groups consecutive frames containing the same detected note and stores basic information such as:

```python
{
    "note": "A4",
    "start": ...,
    "end": ...
}
```

### 🔇 Unvoiced/Silent Frames

Frames where no fundamental frequency is detected are identified separately from detected notes.

---

## ⚠️ Current Limitations

The current prototype still has several technical limitations:

* Pitch detection can contain errors depending on the audio.
* Note boundaries are still being refined.
* Handling of the final detected note needs improvement.
* Rhythm interpretation is not implemented.
* The system is currently monophonic.

---

## 🛠️ Technology

### Currently Used

* **Python**
* **Librosa**
