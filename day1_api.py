"""
Travel Weather Tool
-------------------
Shows weather and country information for any city.

Usage:
    python day3_travel_info.py

Requirements:
    pip install requests python-dotenv
    OPENWEATHER_API_KEY in .env file
    RESTCOUNTRIES_API_KEY in .env file
    """
import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENWEATHER_API_KEY")
rest_api_key = os.getenv("RESTCOUNTRIES_API_KEY")


def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None


def get_country_info(country_code):
    # Use ISO-2 endpoint for v5
    url = f"https://api.restcountries.com/countries/v5/codes.alpha_2/{country_code}"
    headers = {"Authorization": "Bearer " + rest_api_key}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        objects = data.get("data", {}).get("objects", [])
        if objects:
            country = objects[0]
            return {
                "name": country["names"]["common"],
                "region": country.get("region", "Unknown"),
                "population": country.get("population", 0),
                "currency": country["currencies"][0]["code"] if country.get("currencies") else "Unknown"
            }
    return None

def save_data_to_file(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"Data saved to {filename}")
    with open(filename, 'r') as f:
        data = json.load(f)
        



def run_tool():
    print("Travel Weather Tool")
    print("-------------------")
    city = input("Enter a city name: ").strip()

    if not city:
        print("No city entered. Exiting.")
        return

    print(f"\nFetching data for {city}...")

    weather_data = get_weather(city)
    if weather_data:
        save_data_to_file(weather_data, f"{city.lower()}_weather.json")

    if not weather_data:
        print(f"Could not find weather data for '{city}'. Check the city name and try again.")
        return

    # Use ISO code (e.g., KE) from OpenWeatherMap
    country_code = weather_data["sys"]["country"]
    country_data = get_country_info(country_code)

    print(f"\n=== {city.title()}, {country_code} ===")
    print(f"Temperature : {weather_data['main']['temp']} °C")
    print(f"Condition   : {weather_data['weather'][0]['description'].title()}")
    print(f"Humidity    : {weather_data['main']['humidity']}%")
    print(f"Wind        : {weather_data['wind']['speed']} m/s")

    if country_data:
        print(f"\n=== Country Info ===")
        print(f"Country     : {country_data['name']}")
        print(f"Region      : {country_data['region']}")
        print(f"Population  : {country_data['population']:,}")
        print(f"Currency    : {country_data['currency']}")
    else:
        print("Could not fetch country info.")


if __name__ == "__main__":
    run_tool()
