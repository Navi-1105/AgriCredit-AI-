# weather.py
import requests
from config import WEATHER_API_URL, WEATHER_API_KEY

def get_weather_info(location):
    # Construct the API URL for weather data
    api_url = f"{WEATHER_API_URL}{location}?unitGroup=metric&key={WEATHER_API_KEY}&contentType=json"
    
    try:
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()  # Check if the request was successful
        data = response.json()

        # Assuming the weather data returned has these keys:
        # {"temperature_C": 32.0, "rainfall_mm": 10.5, ...}
        return {
            "temperature_C": data['currentConditions']['temp'],
            "rainfall_mm": data['currentConditions']['precip'],
            "location": location
        }
    except requests.exceptions.RequestException as e:
        return {"error": f"Error fetching weather data: {e}"}
    except KeyError:
        return {"error": "Unexpected data format from weather API."}