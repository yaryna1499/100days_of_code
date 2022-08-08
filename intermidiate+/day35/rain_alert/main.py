import requests
import os

def check_rain(hour):
    if weather_data['hourly'][hour]['weather'][0]['id'] >= 700:
        print("Take an umbrella!")


api_key = os.environ.get("api_test_var")
# not working https://guillaume-martin.github.io/saving-environment-variables-in-conda.html

parameters = {
    "lat": 49.553516,
    "lon": 25.594767,
    "appid": api_key,
    "units": "metric",
    "lang": "ua",
    "exclude": "current,minutely,daily"
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()

# print(weather_data['hourly'][0]['weather'][0]['id'])

check_rain(12)

