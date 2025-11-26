import os
import webbrowser

def open_app(app_name):
    try:
        os.system(app_name)
        return f"Opening {app_name}..."
    except:
        return f"Sorry, I couldn’t open {app_name}."

def open_website(url):
    webbrowser.open(url)
    return "Opening website..."
