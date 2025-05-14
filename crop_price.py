# crop_price.py
import requests
from config import CROP_PRICE_API_URL, CROP_PRICE_API_KEY

def get_real_time_crop_price(crop, state):
    # Construct the API URL for real-time crop price
    api_url = f"{CROP_PRICE_API_URL}?crop={crop}&state={state}&key={CROP_PRICE_API_KEY}"
    
    # Send request to the API
    try:
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()  # Check if the request was successful
        data = response.json()
        
        # Assuming the data returned has the structure:
        # {"crop": "Wheat", "price": 2800, "market": "Punjab", "date": "2025-05-14"}
        
        if data and 'price' in data:
            return {
                "market": data.get('market', 'Unknown'),
                "price_rs_per_quintal": data['price'],
                "date": data['date']
            }
        else:
            print(f"No price data found for {crop} in {state}.")
            return {"market": "Unknown", "price_rs_per_quintal": "Not Available", "date": "Not Available"}
    except requests.exceptions.RequestException as e:
        print(f"Error fetching crop price data: {e}")
        return {"market": "Unknown", "price_rs_per_quintal": "Not Available", "date": "Not Available"}
