import datetime
import requests
import os
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_KEY = "GXYSAR582AX7JTFY"
NEWS_KEY = "3e13830801ce46118ed9c51fdf9e1b67"
TWILIO_SID = "ACc2bf3fbbb212db26629d414ac19d76c0"
TWILIO_AUTH_TOKEN = "151af55b7aab37e156511948de8edbf6"

current_date = datetime.datetime.now()
today = str(current_date.strftime("%Y-%m-%d"))
yesterday_date = datetime.datetime(current_date.year, current_date.month, current_date.day-1)
yesterday = str(yesterday_date.strftime("%Y-%m-%d"))
day_before_y_date = datetime.datetime(current_date.year, current_date.month, current_date.day-2)
day_before_y = str(day_before_y_date.strftime("%Y-%m-%d"))


parameters_stock = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_KEY,
}

stock_prices_response = requests.get(url=STOCK_ENDPOINT, params=parameters_stock)
stock_prices_response.raise_for_status()
yesterday_price = stock_prices_response.json()["Time Series (Daily)"][yesterday]["4. close"]
day_before_y_price = stock_prices_response.json()["Time Series (Daily)"][day_before_y]["4. close"]
diff = abs(float(yesterday_price) - float(day_before_y_price))
diff_per_cent = (diff/float(yesterday_price))*100

up_down = None
if diff_per_cent > 0:
    up_down = "🔺"
else:
    up_down = "🔻"


news_params = {
    "qInTitle": COMPANY_NAME,
    "apiKey": NEWS_KEY,
}

articles_response = requests.get(url=NEWS_ENDPOINT, params=news_params)
articles_response.raise_for_status()
articles = articles_response.json()["articles"][:3]
print(articles)

formatted_articles = [f"{STOCK}: {up_down}{diff_per_cent}%\nHeadline: {article['title']}. " \
                      f"\nBrief: {article['description']}" for article in articles]


client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

for article in formatted_articles:
    message = client.messages \
                    .create(
                         body=article,
                         from_='+12104054219',
                         to='+380996457719'
                     )

