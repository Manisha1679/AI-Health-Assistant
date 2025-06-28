# 🩺 Voice-Based Multimodal AI Health Assistant

An AI-powered virtual doctor that listens to the patient's voice, analyzes the image, and replies back with an audio response — just like a real consultation.


## 🧠 Project Overview

This project simulates a real-world telehealth assistant by integrating:

- 🗣️ **Speech Recognition (STT)** – Transcribes patient's voice using Groq's `whisper-large-v3`.
- 🖼️ **Image Understanding (LLM + CV)** – Analyzes facial images using `LLaMA-4 Scout` from Groq.
- 🧾 **Natural Language Understanding & Generation** – AI interprets medical context from text + image.
- 🔊 **Text to Speech (TTS)** – Doctor's reply is converted to speech using Google TTS (`gTTS`).

> This is a **complete AI pipeline** involving **voice input**, **image processing**, **LLM reasoning**, and **voice output**.


## 📦 Tech Stack

| Component | Technology Used |
|----------|-----------------|
| LLM (Multimodal) | `Meta LLaMA-4 Scout via Groq` |
| STT | `Whisper-v3` (Groq API) |
| TTS | `gTTS` (Google Text-to-Speech) |
| Audio Recording | `speech_recognition`, `pyaudio`, `pydub`, `ffmpeg` |
| Image Handling | Base64 Encoding |
| OS Audio Playback | `playsound`, `subprocess`, platform-dependent |


## 🛠️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/voice-ai-health-assistant.git
cd voice-ai-health-assistant
```
### 2. Install Dependencies
Make sure you have Python 3.8+ and install required packages:

```bash
pip install --ignore-pipfile
```
### 3. Set Groq API Key
Create an .env file or set your environment variable:
```.env
 GROQ_API_KEY=your_groq_api_key_here
```
### 4. Configure FFmpeg (for audio)
Download FFmpeg and update the path in voice_patient.py:
```voice_patient.py
AudioSegment.converter = r"C:\path\to\ffmpeg.exe"
```
### 5.Run the app
```bash
python gradio_app.py
```
