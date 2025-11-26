# import requests
# import wikipedia

# def wiki_search(query):
#     try:
#         result = wikipedia.summary(query, sentences=2)
#         return result
#     except Exception:
#         return "Sorry, I couldn't fetch that from Wikipedia."

# def get_weather(city):
#     api_key = "1170320cc36de5223a5cba7980ea24b7"   # ⬅️ Paste your real key here
#     if not city:
#         return "Please tell me the city name to check the weather."
    
#     url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
#     try:
#         response = requests.get(url)
#         data = response.json()
        
#         if data.get("cod") != 200:
#             return f"Sorry, I couldn’t find weather info for {city}."
        
#         weather = data["weather"][0]["description"].capitalize()
#         temp = data["main"]["temp"]
#         feels_like = data["main"]["feels_like"]
#         humidity = data["main"]["humidity"]
        
#         return (
#             f"The weather in {city} is {weather} "
#             f"with a temperature of {temp}°C, feels like {feels_like}°C, "
#             f"and humidity around {humidity}%."
#         )
#     except requests.exceptions.RequestException:
#         return "I couldn’t reach the weather service. Please check your internet connection."



# modules/web_features.py
import requests
import wikipedia

def wiki_search(query):
    if not query:
        return "Please tell me what to search on Wikipedia."
    try:
        return wikipedia.summary(query, sentences=2)
    except Exception as e:
        return f"Could not fetch from Wikipedia: {str(e)}"

def get_weather_openweather(city, api_key):
    if not city:
        return None, "Please say the city name."
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        r = requests.get(url, timeout=6)
        data = r.json()
        if data.get("cod") != 200:
            return None, data.get("message", "City not found.")
        desc = data["weather"][0]["description"].capitalize()
        temp = data["main"]["temp"]
        feels = data["main"].get("feels_like")
        humidity = data["main"].get("humidity")
        resp = f"The weather in {city} is {desc} with a temperature of {temp}°C"
        if feels is not None:
            resp += f", feels like {feels}°C"
        if humidity is not None:
            resp += f", humidity {humidity}%."
        else:
            resp += "."
        return resp, None
    except requests.RequestException:
        return None, "Network error while contacting OpenWeather."

def get_weather_wttr(city):
    # simple fallback using wttr.in (text response)
    if not city:
        return None
    try:
        url = f"http://wttr.in/{city}?format=3"
        r = requests.get(url, timeout=6)
        if r.status_code == 200:
            return r.text  # e.g. "Kolkata: 🌤 +29°C"
        return None
    except Exception:
        return None

def get_weather(city, api_key=None):
    """
    Tries OpenWeather (if api_key provided), else fallback to wttr.in.
    Returns a string answer suitable for speaking.
    """
    city = city.strip()
    if api_key:
        resp, err = get_weather_openweather(city, api_key)
        if resp:
            return resp
        # If invalid API key or other error, fall back
        print("OpenWeather failed:", err)
    # fallback
    wt = get_weather_wttr(city)
    if wt:
        # normalize simple wttr text
        return f"{wt}. (This is a fallback from wttr.in.)"
    return f"Sorry, I couldn't fetch weather for {city}."
