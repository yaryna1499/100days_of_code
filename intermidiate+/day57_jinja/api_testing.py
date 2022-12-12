import requests

gender_response = requests.get("https://api.genderize.io/?name=peter")
gender_response.raise_for_status
print(gender_response.json()["gender"])