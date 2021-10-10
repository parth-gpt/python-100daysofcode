import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

API_KEY = os.environ.get("API_KEY")
LAT = 29.794180
LON = 76.401993
account_sid = os.environ.get("ACC_SID")
auth_token = os.environ.get("AUTH_TOKEN")

parameters = {
    "lat": LAT,
    "lon": LON,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()

weather_data = response.json()

weather_slice = weather_data["hourly"][:12]

################################################ Checking Weather ##############################################

count_rain = 0
count_snow = 0
count_mist = 0
count_smoke = 0
count_haze = 0
count_dust = 0
count_fog = 0
count_dustwind = 0
count_pleasant = 0
count_cloudy = 0

for hour_data in weather_slice:
    weather_id = int(hour_data["weather"][0]["id"])
    if weather_id < 540:
        count_rain += 1
    elif 600 <= weather_id <= 622:
        count_snow += 1
    elif 701 <= weather_id <= 781:
        if weather_id == 701:
            count_mist += 1
        elif weather_id == 711:
            count_smoke += 1
        elif weather_id == 721:
            count_haze += 1
        elif weather_id == 731:
            count_dust += 1
        elif weather_id == 741:
            count_fog += 1
        else:
            count_dustwind += 1
    elif weather_id == 800:
        count_pleasant += 1
    elif weather_id > 800:
        count_cloudy += 1

################################################ Sending Message ##############################################

max_weather = max(count_rain, count_snow, count_mist, count_smoke, count_fog, count_dustwind, count_pleasant,
                  count_cloudy)

if max_weather == count_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
        body="It will rain🌧 today! Don't forget to carry an umbrella☔ or a raincoat.🧥️",
        from_='+18303656120',
        to='+919466847778'
    )
    print(message.status)
elif max_weather == count_snow:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
        body="It's gonna snow!☃️ Carry your snowcoat and umbrella.☔︎",
        from_='+18303656120',
        to='+919466847778'
    )
    print(message.status)
elif max_weather == count_mist:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
        body="There is mist in the air.🌫",
        from_='+18303656120',
        to='+919466847778'
    )
    print(message.status)
elif max_weather == count_smoke:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
        body="There is smoke in the air.💨",
        from_='+18303656120',
        to='+919466847778'
    )
    print(message.status)
elif max_weather == count_haze:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
        body="It's a hazy day!🌫",
        from_='+18303656120',
        to='+919466847778'
    )
    print(message.status)
elif max_weather == count_dust:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
        body="It's a hazy day!🌫",
        from_='+18303656120',
        to='+919466847778'
    )
    print(message.status)
elif max_weather == count_fog:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's a foggy day!🌁",
        from_='+18303656120',
        to='+919466847778'
    )
    print(message.status)
elif max_weather == count_dustwind:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
        body="It's gonna be dust-windy today.🌪",
        from_='+18303656120',
        to='+919466847778'
    )
    print(message.status)
elif max_weather == count_pleasant:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
        body="It's gonna be a pleasant day!🌤",
        from_='+18303656120',
        to='+919466847778'
    )
    print(message.status)
elif max_weather == count_cloudy:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
        body="It is a cloudy day.☁️",
        from_='+18303656120',
        to='+919466847778'
    )
    print(message.status)
