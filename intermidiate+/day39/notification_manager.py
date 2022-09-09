import os
from twilio.rest import Client

TWILIO_SID = "ACc2bf3fbbb212db26629d414ac19d76c0"
TWILIO_AUTH_TOKEN = "151af55b7aab37e156511948de8edbf6"
TWILIO_VIRTUAL_NUMBER = "+12104054219"
TWILIO_VERIFIED_NUMBER = "+380996457719"


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
