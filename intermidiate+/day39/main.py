from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

date_today = datetime.now()
date_to = date_today + timedelta(days=180)

ORIGIN_CITY_IATA = "LON"

data_object = DataManager()
data = data_object.get_data()
flight_object = FlightSearch()
notification = NotificationManager()


if data[0]['iataCode'] == "":
    for row in data:
        row['iataCode'] = flight_object.get_code(row['city'])
    data_object.put_data()

for destination in data:
    flight = flight_object.check_flights(ORIGIN_CITY_IATA,
                                         destination['iataCode'],
                                         date_today, date_to)
    print(flight.price)
    if flight.price < destination['lowestPrice']:
        notification.send_sms(
            message=f"Low price alert! Only {flight.price}EUR to fly from"
                    f" {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}"
                    f"-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        )









