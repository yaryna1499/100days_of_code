import requests
from datetime import datetime
import os

now = datetime.now()
time = now.strftime("%X")
date = now.strftime("%d/%m/%Y")

app_id = os.environ['app_id']
app_key = os.environ['app_key']
username = os.environ['username']
password = os.environ['password']
sheety_url = "https://api.sheety.co/2b913b87a89c663e566916595ae4d0d3/workoutTracking/workouts"

headers = {
    "x-app-id": app_id,
    "x-app-key": app_key,
}

exercises_text = input("Tell me which exercises you did:")

params = {
    "query": exercises_text,
}

url = "https://trackapi.nutritionix.com/v2/natural/exercise"

response = requests.post(url=url, json=params, headers=headers)
result = response.json()
print(result)
contents = {
    "workout": {
        "date": date,
        "time": time,
        "exercise": result['exercises'][0]['name'].title(),
        "duration": int(result['exercises'][0]['duration_min']),
        "calories": int(result['exercises'][0]['nf_calories']),
    }
}

sheet_response = requests.post(url=sheety_url, json=contents, auth=(username, password))
print(sheet_response.text)
