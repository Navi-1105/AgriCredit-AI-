import requests
from config import VISUAL_CROSSING_API_KEY

def get_weather_data(location):
    # Modify URL with the actual location
    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}?unitGroup=metric&key={VISUAL_CROSSING_API_KEY}&contentType=json"
    
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        today = data['days'][0]  # Get today's data
        return {
            "location": location,
            "rainfall_mm": today.get('precip', 0),  # rainfall in mm
            "temperature_C": today.get('temp', 0)   # temperature in °C
        }
    else:
        return {"error": "Failed to fetch data, please check the location or API key."}
