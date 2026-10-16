import requests

url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 0.2827,      # Kakamega latitude
    "longitude": 34.7520,    # Kakamega longitude
    "hourly": "temperature_2m"  # request hourly temperature
}

response = requests.get(url, params=params)

if response.status_code == 200:
     data = response.json()
     todays_temp = data['hourly']['temperature_2m']
     dates = data['hourly']['time']
     Highest_temp = max(todays_temp)
     Lowest_temp = min(todays_temp)
     print("Kakamega Hourly temperatures")
     print("-"*50)
     print("Highest temperature:", Highest_temp)
     print("Lowest temperature:", Lowest_temp)
     for i in range(len(dates)):
         print(f"{dates[i]:<20}{todays_temp[i]:<20}")
     
     print("-"*50)
else:
     print("request failed:", response.status_code)
