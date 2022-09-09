import requests


SHEETY_ENDPOINT = "https://api.sheety.co/2b913b87a89c663e566916595ae4d0d3/flightDeals/prices"


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}

    def get_data(self):
        response = requests.get(SHEETY_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def put_data(self):
        for row in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": row["iataCode"]
                }
            }
            response = requests.put(url=f"{SHEETY_ENDPOINT}/{row['id']}", json=new_data)
            print(response.text)
