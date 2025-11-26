# modules/emotion_detector.py

import numpy as np

def analyze_emotion(audio_data):
    """
    Takes raw microphone audio data and returns an emotional guess:
    happy / excited / tired / sad / neutral / stressed.
    """

    # Convert audio to numpy array
    audio_array = np.frombuffer(audio_data.frame_data, dtype=np.int16)

    # Basic acoustic features
    volume = np.abs(audio_array).mean()
    energy = np.sum(audio_array ** 2) / len(audio_array)

    # Thresholds tuned by testing
    if volume < 200:
        return "tired"
    if energy < 500000:
        return "sad"
    if volume > 5000 and energy > 10000000:
        return "excited"
    if 3000 < volume < 5000:
        return "happy"
    if energy > 7000000 and volume > 3500:
        return "stressed"

    return "neutral"
