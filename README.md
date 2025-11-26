📘 README.md — Jarvis 2.0 (Voice Assistant)
# 🧠 Jarvis 2.0 — Voice-Controlled Desktop AI Assistant

Jarvis 2.0 is an offline-capable, voice-controlled desktop assistant written in Python.  
It listens, speaks, searches information, remembers facts, fetches weather, controls applications, manages tasks, and more.  
Inspired by Tony Stark’s JARVIS from Iron Man. 🚀

---

## 🎥 Demo GIF (Add your GIF here)

<p align="center">
  <img src="asset/jarvis.gif" width="900">
</p>

---

## ✨ Features

### 🎤 Voice Interaction
- Listens to voice commands using SpeechRecognition  
- Speaks responses using pyttsx3  
- Works offline except weather & Wikipedia  
- Stable, fast, and no API needed

### 📚 Knowledge & Memory
- “Remember my birthday is 5th May”
- “What is my birthday?”
- Saves memory permanently in `memory.json`

### 🌦 Weather Information
- “What’s the weather in Kolkata?”
- Uses OpenWeather API or fallback to wttr.in  
- Works even without an API key

### 🌐 Wikipedia Search
- “Explain entropy”
- “Tell me about Python programming”
- Gives 2–3 sentence summary

### 💻 System App Controls
Open apps:
- YouTube  
- WhatsApp Web  
- Browser  
- Chrome  
- Edge  
- Word  
- PowerPoint  
- Paint  
- VS Code  

Close apps:
- Chrome  
- Edge  
- Word  
- PowerPoint  
- Paint  
- VS Code  

### 🎵 Music Playback
- “Play music”  
- Plays a random song from your default music folder

### 📝 Task Manager
- “Add task complete assignment”  
- “Show tasks”  
- “Clear tasks”  
- Tasks saved in `tasks.txt`

### 🧠 Smart Offline Logic
- When Wikipedia fails → Gives intelligent fallback responses  
- Fully offline reasoning  
- No DeepSeek / GPT / Gemini needed

---

## 📂 Folder Structure



Jarvis/
│
├── main.py
├── README.md
│
├── modules/
│ ├── ai_core.py
│ ├── knowledge.py
│ ├── system_control.py
│ ├── web_features.py
│ ├── speech_listener.py
│ └── voice_engine.py
│
└── data/
├── memory.json
└── tasks.txt


---

## 🛠 Installation

### 🔧 1. Install Requirements

```bash
pip install pyttsx3 SpeechRecognition requests wikipedia PyAudio


If PyAudio fails (Windows):

pip install pipwin
pipwin install pyaudio

