import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "41HAPDFEEIGCEA4Q"
NEWS_API_KEY = "99febef9d8dd4b3caf45dbff8b2c48dc"

account_sid = "AC7da2cbb5b50b5fe6a2c480f21536669b"
auth_token = {Auth_Token}

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "TSLA",
    "apikey": STOCK_API_KEY
}

response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
response.raise_for_status()

stock_data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in stock_data.items()][:2]

yesterday_closing = data_list[0]["4. close"]
day_before_yesterday_closing = data_list[1]["4. close"]

difference = float(yesterday_closing) - float(day_before_yesterday_closing)

up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

diff_percent = round((abs(difference) / float(yesterday_closing)) * 100)

if diff_percent > 0.5:
    news_parameters = {
        "qInTitle": COMPANY_NAME,
        "apiKey": NEWS_API_KEY
    }

    response = requests.get(NEWS_ENDPOINT, params=news_parameters)
    response.raise_for_status()

    news_data = response.json()["articles"][:3]

    refined_news_data = [f"{STOCK}: {up_down}{diff_percent}% \nHeadline: {article['title']}. \nBrief: {article['description']}" for article in news_data]

    client = Client(account_sid, auth_token)
    for article in refined_news_data:
        message = client.messages \
            .create(
            body=article,
            from_='+18303656120',
            to='+919466847778'
        )
        print(message.status)
