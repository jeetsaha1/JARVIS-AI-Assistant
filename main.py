# # main.py
# import time
# from modules.voice_engine import speak
# from modules.speech_listener import listen
# from modules import knowledge, web_features, system_control, ai_core, utils
# from datetime import datetime

# # Put your OpenWeather API key here or set OPENWEATHER_KEY environment variable
# import os
# OPENWEATHER_KEY = os.environ.get("OPENWEATHER_KEY") or ""  # or paste your key string here

# # Keep a small in-memory conversation history for context (limits size)
# conversation_history = []

# def process_command(cmd):
#     cmd = cmd.lower().strip()
#     if not cmd:
#         return None

#     # greetings
#     if any(w in cmd for w in ["hello", "hi jarvis", "hey jarvis", "hi"]):
#         return "Hello Jeet! How can I help you today?"

#     # time / date
#     if "time" in cmd and ("what" in cmd or "tell" in cmd or "current" in cmd or cmd == "time"):
#         return f"The current time is {datetime.now().strftime('%H:%M:%S')}."

#     if "date" in cmd:
#         return f"Today's date is {datetime.now().strftime('%A, %d %B %Y')}."

#     # remember facts: "remember my favorite color is blue" or "remember favorite color is blue"
#     if "remember" in cmd and " is " in cmd:
#         try:
#             left, right = cmd.split("remember",1)[1].split(" is ",1)
#             key = left.strip()
#             value = right.strip()
#             return knowledge.learn_fact(key, value)
#         except Exception:
#             # alternative simple parsing
#             rest = utils.extract_after_keyword(cmd, "remember")
#             if " is " in rest:
#                 key, value = rest.split(" is ",1)
#                 return knowledge.learn_fact(key.strip(), value.strip())
#             return "Tell me in format: remember <key> is <value>."

#     # recall: "what is my favorite color" or "what is <key>"
#     if cmd.startswith("what is") or cmd.startswith("who is") or cmd.startswith("tell me about"):
#         # check memory first
#         key = cmd.replace("what is", "").replace("who is", "").replace("tell me about", "").strip()
#         memval = knowledge.recall_fact(key)
#         if memval:
#             return f"{key} is {memval}."
#         # else fallback to wiki (or AI)
#         wiki_ans = web_features.wiki_search(key)
#         return wiki_ans

#     # weather queries: "what's the weather in kolkata" or "weather in kolkata"
#     if "weather" in cmd:
#         city = ""
#         if " in " in cmd:
#             city = cmd.split(" in ",1)[1].strip()
#         elif "weather" != cmd:
#             # try to catch "kolkata weather"
#             parts = cmd.split()
#             for i,p in enumerate(parts):
#                 if p == "weather" and i>0:
#                     city = parts[i-1]
#                     break
#         if not city:
#             return "Please tell me the city name. Example: what's the weather in Kolkata?"
#         return web_features.get_weather(city, api_key=OPENWEATHER_KEY)

#     # tasks
#     if cmd.startswith("add task") or cmd.startswith("add to do") or ("add" in cmd and "task" in cmd):
#         # format: "add task buy milk"
#         task = cmd.replace("add task", "").replace("add to do", "").replace("add", "").replace("task", "").strip()
#         if not task:
#             return "Please say the task to add."
#         return knowledge.add_task(task)

#     if "show tasks" in cmd or "list tasks" in cmd or ("what" in cmd and "task" in cmd):
#         tasks = knowledge.list_tasks()
#         if not tasks:
#             return "You have no tasks."
#         return "Your tasks are: " + "; ".join(tasks)

#     if "clear tasks" in cmd or "delete tasks" in cmd:
#         return knowledge.clear_tasks()

#     # open / close apps
#     if cmd.startswith("open ") or ("open" in cmd and any(k in cmd for k in ["youtube","chrome","edge","word","code","paint"])):
#         return system_control.open_app(cmd)

#     if cmd.startswith("close ") or ("close" in cmd and any(k in cmd for k in ["close","shutdown tab","close chrome","close edge"])):
#         return system_control.close_app(cmd)

#     if "play music" in cmd or "play song" in cmd:
#         return system_control.play_music()

#     # Exit
#     if any(w in cmd for w in ["exit", "quit", "stop listening", "goodbye", "bye jarvis"]):
#         speak("Goodbye Jeet. I will be here when you need me.")
#         exit(0)

#     # If user asked for AI-style chat or general question -> use ai_core
#     # We'll keep conversation_history short (max 8 messages)
#     global conversation_history
#     # add user message to history as Chat API expects
#     conversation_history.append({"role":"user","content":cmd})
#     if len(conversation_history) > 8:
#         # drop oldest
#         conversation_history = conversation_history[-8:]
#     ai_response = ai_core.ai_chat(cmd, conversation_history)
#     # append assistant reply to history for better context next time
#     conversation_history.append({"role":"assistant","content":ai_response})
#     if len(conversation_history) > 16:
#         conversation_history = conversation_history[-16:]
#     return ai_response

# def main_loop():
#     speak("Initializing Jarvis 2.0. Hello Jeet!")
#     while True:
#         try:
#             # listen with a short timeout so loop keeps running smoothly
#             user_cmd = listen(timeout=6, phrase_time_limit=8)
#             if not user_cmd:
#                 # No input - continue listening
#                 continue
#             response = process_command(user_cmd)
#             if response:
#                 print("🤖 Jarvis:", response)
#                 speak(response)
#             # short pause to avoid re-triggering on noise
#             time.sleep(0.4)
#         except KeyboardInterrupt:
#             speak("Shutting down. Bye.")
#             break
#         except Exception as e:
#             print("Error in main loop:", e)
#             speak("I encountered an error. Please check the console.")

# if __name__ == "__main__":
#     main_loop()

















import time
from modules.voice_engine import speak
from modules.speech_listener import listen
from modules import knowledge, web_features, system_control, ai_core, utils
from datetime import datetime

# Put your OpenWeather API key here or set OPENWEATHER_KEY environment variable
import os
OPENWEATHER_KEY = os.environ.get("OPENWEATHER_KEY") or ""  # or paste your key string here

# Keep a small in-memory conversation history for context (limits size)
conversation_history = []

def process_command(cmd):
    cmd = cmd.lower().strip()
    if not cmd:
        return None

    # greetings
    if any(w in cmd for w in ["hello", "hi jarvis", "hey jarvis", "hi"]):
        return "Hello Jeet! How can I help you today?"

    # time / date
    if "time" in cmd and ("what" in cmd or "tell" in cmd or "current" in cmd or cmd == "time"):
        return f"The current time is {datetime.now().strftime('%H:%M:%S')}."

    if "date" in cmd:
        return f"Today's date is {datetime.now().date()}"

    # remember facts: "remember my favorite color is blue" or "remember favorite color is blue"
    if "remember" in cmd and " is " in cmd:
        try:
            left, right = cmd.split("remember",1)[1].split(" is ",1)
            key = left.strip()
            value = right.strip()
            return knowledge.learn_fact(key, value)
        except Exception:
            # alternative simple parsing
            rest = utils.extract_after_keyword(cmd, "remember")
            if " is " in rest:
                key, value = rest.split(" is ",1)
                return knowledge.learn_fact(key.strip(), value.strip())
            return "Tell me in format: remember <key> is <value>."

    # recall: "what is my favorite color" or "what is <key>"
    if cmd.startswith("what is") or cmd.startswith("who is") or cmd.startswith("tell me about"):
        # check memory first
        key = cmd.replace("what is", "").replace("who is", "").replace("tell me about", "").strip()
        memval = knowledge.recall_fact(key)
        if memval:
            return f"{key} is {memval}."
        # else fallback to wiki (or AI)
        wiki_ans = web_features.wiki_search(key)
        return wiki_ans

    # weather queries: "what's the weather in kolkata" or "weather in kolkata"
    if "weather" in cmd:
        city = ""
        if " in " in cmd:
            city = cmd.split(" in ",1)[1].strip()
        elif "weather" != cmd:
            # try to catch "kolkata weather"
            parts = cmd.split()
            for i,p in enumerate(parts):
                if p == "weather" and i>0:
                    city = parts[i-1]
                    break
        if not city:
            return "Please tell me the city name. Example: what's the weather in Kolkata?"
        return web_features.get_weather(city, api_key=OPENWEATHER_KEY)

    # tasks
    if cmd.startswith("add task") or cmd.startswith("add to do") or ("add" in cmd and "task" in cmd):
        # format: "add task buy milk"
        task = cmd.replace("add task", "").replace("add to do", "").replace("add", "").replace("task", "").strip()
        if not task:
            return "Please say the task to add."
        return knowledge.add_task(task)

    if "show tasks" in cmd or "list tasks" in cmd or ("what" in cmd and "task" in cmd):
        tasks = knowledge.list_tasks()
        if not tasks:
            return "You have no tasks."
        return "Your tasks are: " + "; ".join(tasks)

    if "clear tasks" in cmd or "delete tasks" in cmd:
        return knowledge.clear_tasks()

    # open / close apps
    if cmd.startswith("open ") or ("open" in cmd and any(k in cmd for k in ["youtube","chrome","edge","word","code","paint"])):
        return system_control.open_app(cmd)

    if cmd.startswith("close ") or ("close" in cmd and any(k in cmd for k in ["close","shutdown tab","close chrome","close edge"])):
        return system_control.close_app(cmd)

    if "play music" in cmd or "play song" in cmd:
        return system_control.play_music()

    # Exit
    if any(w in cmd for w in ["exit", "quit", "stop listening", "goodbye", "bye jarvis"]):
        speak("Goodbye Jeet. I will be here when you need me.")
        exit(0)

    # If user asked for AI-style chat or general question -> use ai_core
    # We'll keep conversation_history short (max 8 messages)
    global conversation_history
    # add user message to history as Chat API expects
    conversation_history.append({"role":"user","content":cmd})
    if len(conversation_history) > 8:
        # drop oldest
        conversation_history = conversation_history[-8:]
    ai_response = ai_core.ai_chat(cmd, conversation_history)
    # append assistant reply to history for better context next time
    conversation_history.append({"role":"assistant","content":ai_response})
    if len(conversation_history) > 16:
        conversation_history = conversation_history[-16:]
    return ai_response

def main_loop():
    speak("Initializing Jarvis 2.0. Hello Jeet!")
    while True:
        try:
            # listen with a short timeout so loop keeps running smoothly
            result = listen(timeout=6, phrase_time_limit=8)

            # FIX: handle (text, emotion) or just text
            if isinstance(result, tuple):
                user_cmd, emotion = result
            else:
                user_cmd = result
                emotion = None

            if not user_cmd:
                continue

            response = process_command(user_cmd)

            if response:
                print("🤖 Jarvis:", response)
                speak(response)

            # short pause to avoid re-triggering on noise
            time.sleep(0.4)

        except KeyboardInterrupt:
            speak("Shutting down. Bye.")
            break

        except Exception as e:
            print("Error in main loop:", e)
            speak("I encountered an error. Please check the console.")


if __name__ == "__main__":
    main_loop()
