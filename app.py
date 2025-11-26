from flask import Flask, render_template, jsonify
from modules.speech_listener import listen
from modules.voice_engine import speak
from modules import ai_core

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/listen')
def get_voice():
    command = listen()
    response = ai_core(command)
    speak(response)
    return jsonify({"user": command, "jarvis": response})

if __name__ == "__main__":
    app.run(debug=True)
