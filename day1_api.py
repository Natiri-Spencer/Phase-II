import requests
import os
from dotenv import load_dotenv

load_dotenv()

response = requests.get(
    'https://api.restcountries.com/countries/v5?q=kenya',
    headers={'Authorization': "Bearer " + os.environ["RESTCOUNTRIES_API_KEY"]}
)

if response.status_code == 200:
    data = response.json()

    # Navigate into the nested structure
    objects = data.get("data", {}).get("objects", [])
    if objects:
        country = objects[0]  # first country object

        name = country["names"]["common"]
        capital = country["capitals"][0]["name"]
        alternate_names = country['names']['alternates']
        population = country["population"]
        currency = country["currencies"][0]["code"]

        print(f"country: {name}")
        print(f"Alternate name: {alternate_names[0]}")
        print(f"capital: {capital}")
        print(f"population: {population}")
        
        print(f"currency: {currency}")
    else:
        print("No country objects found in response.")
else:
    print(f"Request failed. Status: {response.status_code}")

