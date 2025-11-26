import os
import subprocess
import random
import psutil  # For listing running processes

def open_app(command):
    cmd = command.lower()
    if "youtube" in cmd:
        os.system("start https://www.youtube.com")
        return "Opening YouTube."
    elif "whatsapp" in cmd:
        os.system("start https://web.whatsapp.com/")
        return "Opening WhatsApp Web."
    elif "chatgpt" in cmd or "chat" in cmd:
        os.system("start https://chat.openai.com/")
        return "Opening ChatGPT."
    elif "browser" in cmd or "google" in cmd:
        os.system("start https://www.google.com")
        return "Opening your browser."
    elif "word" in cmd:
        os.system("start winword")
        return "Opening Microsoft Word."
    elif "powerpoint" in cmd or "ppt" in cmd:
        os.system("start powerpnt")
        return "Opening PowerPoint."
    elif "paint" in cmd:
        os.system("start mspaint")
        return "Opening Paint."
    elif "code" in cmd or "vscode" in cmd:
        try:
            os.system("start code")
            return "Opening Visual Studio Code."
        except Exception:
            return "Couldn't start VS Code. Make sure 'code' is in PATH."
    elif "edge" in cmd:
        os.system("start msedge")
        return "Opening Microsoft Edge."
    elif "chrome" in cmd:
        os.system("start chrome")
        return "Opening Google Chrome."
    elif "explorer" in cmd or "file explorer" in cmd:
        os.system("start explorer")
        return "Opening File Explorer."
    elif "notepad" in cmd:
        os.system("start notepad")
        return "Opening Notepad."
    else:
        return "Sorry, I don't know how to open that application."

def close_app(command):
    cmd = command.lower()

    app_processes = {
        "chrome": ["chrome.exe"],
        "edge": ["msedge.exe"],
        "word": ["winword.exe"],
        "powerpoint": ["powerpnt.exe"],
        "paint": ["mspaint.exe"],
        "vscode": ["code.exe", "Code.exe", "Code - Insiders.exe"],
        "explorer": ["explorer.exe"],
        "notepad": ["notepad.exe"],
        "youtube": ["chrome.exe", "msedge.exe"],  # closes browser tabs
        "whatsapp": ["chrome.exe", "msedge.exe"], # closes browser tabs
    }

    try:
        for key, processes in app_processes.items():
            if key in cmd:
                closed_any = False
                for process in processes:
                    result = os.system(f"taskkill /f /im \"{process}\" >nul 2>&1")
                    if result == 0:
                        closed_any = True
                if closed_any:
                    return f"Closed {key.capitalize()}."
                else:
                    return f"{key.capitalize()} doesn't seem to be open right now."
        return "I couldn't find that app running or I don't have a rule for it."
    except Exception as e:
        return f"Failed to close app: {e}"


def show_tasks():
    """Returns a list of active applications (top-level window titles)."""
    try:
        running_apps = []
        for proc in psutil.process_iter(['pid', 'name']):
            if proc.info['name'] and proc.info['name'].endswith('.exe'):
                running_apps.append(proc.info['name'])
        if not running_apps:
            return "No active apps found."
        apps_list = sorted(set(running_apps))
        return "Currently running apps include:\n" + "\n".join(apps_list[:20])  # limit for readability
    except Exception as e:
        return f"Error showing tasks: {e}"

def play_music(folder_path=None):
    if not folder_path:
        folder_path = "C:/Users/Public/Music"
    if not os.path.exists(folder_path):
        return "Music folder not found."
    files = [f for f in os.listdir(folder_path) if not f.startswith(".")]
    if not files:
        return "No music files found."
    song = random.choice(files)
    try:
        os.startfile(os.path.join(folder_path, song))
        return f"Playing {song}."
    except Exception:
        return "Could not play music."
