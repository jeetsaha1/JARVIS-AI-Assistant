import speech_recognition as sr
from modules.emotion_detector import analyze_emotion

def listen(timeout=7, phrase_time_limit=8):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        audio = r.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)

    try:
        text = r.recognize_google(audio)
        print("🗣 You said:", text)

        # Emotion detection
        emotion = analyze_emotion(audio)

        return text, emotion

    except:
        return None, "neutral"
