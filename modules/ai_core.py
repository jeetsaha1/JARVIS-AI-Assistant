# # modules/ai_core.py
# import os

# OPENAI_KEY = os.environ.get("OPENAI_API_KEY") or None

# def ai_chat(prompt, conversation_history=None, max_tokens=300):
#     """
#     If OPENAI_API_KEY is set in environment, use ChatCompletion API to generate
#     context-aware responses. conversation_history is list of dict messages if present.
#     If no key, fall back to a simple rule-based reply.
#     """
#     if not prompt:
#         return "Please say something so I can help."
#     if OPENAI_KEY:
#         try:
#             import openai
#             openai.api_key = OPENAI_KEY
#             messages = [{"role":"system","content":"You are Jarvis, a helpful conversational AI assistant."}]
#             if conversation_history:
#                 messages.extend(conversation_history)
#             messages.append({"role":"user","content":prompt})
#             resp = openai.ChatCompletion.create(
#                 model="gpt-3.5-turbo",
#                 messages=messages,
#                 max_tokens=max_tokens,
#                 temperature=0.7
#             )
#             return resp["choices"][0]["message"]["content"].strip()
#         except Exception as e:
#             print("OpenAI error:", e)
#             # fallback
#     # Simple fallback rule-based responses:
#     lower = prompt.lower()
#     if "joke" in lower:
#         return "Why did the programmer quit his job? Because he didn't get arrays."
#     if "your name" in lower or "who are you" in lower:
#         return "I am Jarvis, your personal assistant."
#     if "time" in lower or "date" in lower:
#         from datetime import datetime
#         return f"The current time is {datetime.now().strftime('%H:%M:%S')} on {datetime.now().strftime('%d %B %Y')}."
#     # default reply
#     return "I can help with weather, controlling apps, searching Wikipedia, and chit-chat. Try asking me something specific."


import random
import datetime

def ai_chat(command: str, context=None) -> str:

    """Basic conversational AI logic"""

    command = command.lower()

    # Greetings
    if any(word in command for word in ["hello", "hi", "hey"]):
        return random.choice([
            "Hello Jeet! How can I assist you today?",
            "Hi there! Jarvis is online and ready.",
            "Hey Jeet! What’s up?"
        ])

    # Jokes
    if "joke" in command:
        return get_joke()

    # Time and Date
    if "time" in command:
        return f"The current time is {datetime.datetime.now().strftime('%I:%M %p')}."
    if "date" in command:
        return f"Today's date is {datetime.datetime.now().strftime('%A, %d %B %Y')}."

    # Compliments or chatter
    if "how are you" in command:
        return "I’m just a bunch of code, but I’m feeling quite operational, thanks!"
    if "thank" in command:
        return random.choice(["You're welcome!", "Anytime, Jeet!", "Glad to help!"])
    if "who created you" in command:
        return "I was created by Tony Stark—well, sort of. In this version, by Jeet Saha!"
    if "what can you do" in command:
        return "I can tell jokes, fetch weather, control apps, and chat with you in real time."

    # Unknown input
    return random.choice([
        "I’m not sure I understand that.",
        "Can you please repeat that?",
        "Hmm... that’s interesting. Could you clarify?"
    ])


def get_joke() -> str:
    """Return a random clean joke"""
    jokes = [
        "Why did the computer show up at work late? It had a hard drive!",
        "I told my computer I needed a break, and it said 'You seem stressed, shall I close your tabs?'",
        "Why was the JavaScript developer sad? Because they didn’t Node how to Express themselves!",
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "Parallel lines have so much in common… it’s a shame they’ll never meet."
    ]
    return random.choice(jokes)
