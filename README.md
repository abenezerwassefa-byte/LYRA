# 🎵 LYRA

**LYRA** is an AI-assisted music transcription project that analyzes piano audio and converts detected pitches into structured musical note data.

> 🚧 **Status:** Early-stage development
> **Current focus:** Audio analysis and basic monophonic note detection

## 🎯 Overview

The goal of LYRA is to explore how audio-processing and machine-learning techniques can be used to transform musical audio into structured notation.

The current implementation focuses on the first stage of this process: extracting pitch information from an audio file and identifying basic musical notes.

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

## 🚧 Not Yet Implemented

The following components are **not currently implemented**.

### 🔥 PyTorch

PyTorch has **not yet been implemented** in the LYRA codebase.

It is intended for future experimentation with machine-learning and deep-learning approaches to improve transcription.

### 📊 Matplotlib

Matplotlib has **not yet been implemented**.

It may be used later to visualize audio-analysis results such as pitch contours and detected notes.

### 🎹 Polyphonic Transcription

The current system is monophonic.

It cannot reliably identify multiple notes being played simultaneously, such as chords.

### 🥁 Rhythm and Note-Value Detection

LYRA currently detects pitch and basic timing information, but it does not yet determine musical note values such as:

* Quarter notes
* Eighth notes
* Half notes
* Dotted notes

### 🎼 Complete Sheet-Music Generation

The project does not yet convert detected notes into complete, properly formatted sheet music.

### 🎹 MIDI Export

MIDI generation and export have not yet been implemented.

### 🎼 Key and Time-Signature Detection

The system does not currently determine:

* Musical key
* Time signature
* Measures/bars

### 🧠 Trained Transcription Model

There is currently no trained deep-learning music-transcription model integrated into LYRA.

### 🌐 Web Application

A web application is **not part of the planned LYRA implementation**.

LYRA is focused on the underlying audio-analysis, music-processing, and AI/ML aspects of transcription rather than building a web platform.

---

## ⚠️ Current Limitations

The current prototype still has several technical limitations:

* Pitch detection can contain errors depending on the audio.
* Note boundaries are still being refined.
* Handling of the final detected note needs improvement.
* Rhythm interpretation is not implemented.
* The system is currently monophonic.
* There are currently no formal evaluation metrics or benchmark results.
* The implementation is still experimental and has not been optimized for production use.

---

## 🛠️ Technology

### Currently Used

* **Python**
* **Librosa**
* **NumPy**

### Planned / Not Yet Implemented

* **PyTorch**
* **Matplotlib**

The technology list reflects the actual implementation status rather than technologies that are merely planned.

---

## 🗺️ Roadmap

### Phase 1 — Audio Analysis

* [x] Load audio
* [x] Preserve original sample rate
* [x] Estimate fundamental frequency
* [x] Convert frequency to musical notes
* [x] Map detected notes to timestamps
* [x] Basic monophonic note segmentation
* [ ] Improve note-boundary handling
* [ ] Improve handling of rests and silent sections

### Phase 2 — Musical Representation

* [ ] Improve note duration detection
* [ ] Detect rhythmic values
* [ ] Detect tempo
* [ ] Detect key
* [ ] Detect time signature
* [ ] Represent notes in a more complete musical structure

### Phase 3 — Machine Learning

* [ ] Integrate PyTorch
* [ ] Experiment with machine-learning/deep-learning approaches
* [ ] Evaluate model performance
* [ ] Investigate improved pitch/transcription methods

### Phase 4 — Output

* [ ] Generate structured musical notation
* [ ] Implement MIDI export
* [ ] Improve sheet-music representation

### Phase 5 — Polyphonic Transcription

* [ ] Detect multiple simultaneous notes
* [ ] Handle chords
* [ ] Improve transcription of more complex piano recordings

---

## 📌 Project Status

LYRA is an **active work-in-progress**.

The current milestone is establishing a reliable foundation for audio analysis and **basic monophonic note detection**.

The project will progressively move from signal processing toward machine-learning-based approaches and more complete musical representation.

**No web application is planned for LYRA.** The project is focused on the core transcription technology.
