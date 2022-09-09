import requests
from flight_data import FlightData

FLIGHT_ENDPOINT = "https://tequila-api.kiwi.com"
FLIGHT_KEY = "2zDP7Sc8GWGDNrJF4iSMxmY9M_kq8m63"


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def get_code(self, city_name):
        header = {"apikey": FLIGHT_KEY}
        parameters = {"term": city_name, "location_types": "city"}
        flight_response = requests.get(f"{FLIGHT_ENDPOINT}/locations/query", params=parameters, headers=header)
        code = flight_response.json()['locations'][0]['code']
        return code

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        header = {"apikey": FLIGHT_KEY}
        parameters = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "EUR"
        }

        response = requests.get(f"{FLIGHT_ENDPOINT}/v2/search", params=parameters, headers=header)

        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None
        else:
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0]
            )
            return flight_data

        print(f"{flight_data.destination_city}: €{flight_data.price}")
        return flight_data




