import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENWEATHER_API_KEY")
country_api_key = os.getenv("RESTCOUNTRIES_API_KEY")


def get_weather(city):
    url = "https://api.openweathermap.org/data/2.5/weather"
    try:
        response = requests.get(
            url, params={"q": city, "appid": api_key, "units": "metric"}, timeout=15
        )
        response.raise_for_status()
        return response.json()
    except (requests.RequestException, ValueError):
        return None
    return None


def get_country_info(country_code):
    if not country_api_key:
        print("Add RESTCOUNTRIES_API_KEY to your .env file to fetch country information.")
        return None
    url = f"https://api.restcountries.com/countries/v5/codes.alpha_2/{country_code}"
    try:
        response = requests.get(
            url, headers={"Authorization": f"Bearer {country_api_key}"}, timeout=15
        )
        response.raise_for_status()
        data = response.json()
    except (requests.RequestException, ValueError):
        return None

    # v5 wraps country records inside data.objects.
    if isinstance(data, dict) and isinstance(data.get("data"), dict):
        countries = data["data"].get("objects", [])
        if isinstance(countries, list) and countries and isinstance(countries[0], dict):
            return countries[0]
    return None


def run_tool():
    print("Travel Weather Tool")
    print("-------------------")
    city = input("Enter a city name: ").strip()

    if not city:
        print("No city entered. Exiting.")
        return

    print(f"\nFetching data for {city}...")

    weather_data = get_weather(city)

    if not weather_data:
        print(f"Could not find weather data for '{city}'. Check the city name and try again.")
        return

    country_code = weather_data["sys"]["country"]
    country_data = get_country_info(country_code)

    print(f"\n=== {city.title()}, {country_code} ===")
    print(f"Temperature : {weather_data['main']['temp']}C")
    print(f"Condition   : {weather_data['weather'][0]['description'].title()}")
    print(f"Humidity    : {weather_data['main']['humidity']}%")
    print(f"Wind        : {weather_data['wind']['speed']} m/s")

    if country_data:
        population = country_data.get("population")
        population_text = f"{population:,}" if isinstance(population, (int, float)) else "Unknown"
        region = country_data.get("region") or "Unknown"
        currencies = ", ".join(
            currency["code"] for currency in (country_data.get("currencies") or [])
            if isinstance(currency, dict) and currency.get("code")
        ) or "Unknown"
        print(f"\n=== Country Info ===")
        print(f"Region      : {region}")
        print(f"Population  : {population_text}")
        print(f"Currency    : {currencies}")
    else:
        print("\nCountry information is currently unavailable.")


if __name__ == "__main__":
    run_tool()
