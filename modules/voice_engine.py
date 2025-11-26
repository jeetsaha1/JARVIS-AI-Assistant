# # modules/voice_engine.py
# import pyttsx3
# import os
# from playsound import playsound
# from tempfile import NamedTemporaryFile

# _engine = None

# def _get_engine():
#     global _engine
#     if _engine is None:
#         _engine = pyttsx3.init()
#         _engine.setProperty('rate', 170)  # slightly slower for clarity
#         voices = _engine.getProperty('voices')
#         # choose male voice if available (voices[0] usually male on Windows)
#         try:
#             _engine.setProperty('voice', voices[0].id)
#         except Exception:
#             pass
#     return _engine

# def speak(text, use_tts_engine=True):
#     """
#     Speak text. Default uses pyttsx3 (fast, offline). If you prefer
#     gTTS audio (more natural), set use_tts_engine=False (requires internet).
#     """
#     if not text:
#         return
#     if use_tts_engine:
#         engine = _get_engine()
#         engine.say(text)
#         engine.runAndWait()
#     else:
#         # fallback: use gTTS for more natural voice (requires internet)
#         try:
#             from gtts import gTTS
#             tmp = NamedTemporaryFile(delete=False, suffix=".mp3")
#             tts = gTTS(text=text, lang="en")
#             tts.save(tmp.name)
#             playsound(tmp.name)
#             tmp.close()
#             os.remove(tmp.name)
#         except Exception:
#             # final fallback to pyttsx3
#             engine = _get_engine()
#             engine.say(text)
#             engine.runAndWait()


import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 180)
engine.setProperty('voice', engine.getProperty('voices')[1].id)  # female voice

def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()
