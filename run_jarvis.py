import subprocess
import time

# Start Flask web app first
print("🚀 Starting Jarvis web interface...")
flask_process = subprocess.Popen(["python", "app.py"])

# Wait a few seconds for the web server to load
time.sleep(3)

# Then start voice assistant
print("🎙️ Starting Jarvis voice assistant...")
voice_process = subprocess.Popen(["python", "main.py"])

try:
    flask_process.wait()
    voice_process.wait()
except KeyboardInterrupt:
    print("🛑 Shutting down Jarvis...")
    flask_process.terminate()
    voice_process.terminate()
