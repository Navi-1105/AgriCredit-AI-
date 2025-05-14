from crop_price import get_real_time_crop_price
from loan_engine import get_credit_advice
from weather import get_weather_info

def main():
    # User input for city, crop, land size, and state
    location = input("Enter your city or district (e.g., Fatehgarh Sahib): ")
    crop = input("Enter your crop (e.g., Wheat, Rice, etc.): ")
    state = input("Enter your state (e.g., Punjab, Haryana, Maharashtra): ")
    land_size = float(input("Enter your land size in acres: "))
    
    # Fetch weather data
    weather = get_weather_info(location)
    if 'error' in weather:
        print(weather['error'])
    else:
        print(f"\n--- Weather Info for {location} ---")
        print(f"Rainfall: {weather['rainfall_mm']} mm")
        print(f"Temperature: {weather['temperature_C']} °C")

    # Fetch real-time crop price data
    crop_price_data = get_real_time_crop_price(crop, state)
    print(f"\n--- Crop Price Info ---")
    print(f"Market: {crop_price_data['market']}")
    print(f"Price: ₹{crop_price_data['price_rs_per_quintal']} per quintal")
    print(f"Date: {crop_price_data['date']}")

    # Get loan eligibility and recommendation
    loan_advice = get_credit_advice(land_size, weather['rainfall_mm'], crop_price_data['price_rs_per_quintal'])
    print(f"\n--- Loan Recommendation ---")
    print(loan_advice)

if __name__ == "__main__":
    main()
