# config.py

# Weather API Configuration
WEATHER_API_URL = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"
WEATHER_API_KEY = "WZAB5RSJU7RDV3KGTTDVGX7TG"

# Crop Price API Configuration (Example: eNAM API)
CROP_PRICE_API_URL = "https://api.enam.gov.in/v1/crop_prices"
CROP_PRICE_API_KEY = "your_enam_api_key_here"  # If you have an API key for eNAM or any other crop price API

# Optionally, you can add other config values like timeouts or parameters
TIMEOUT = 10  # Set a timeout for the API calls to avoid long waits
