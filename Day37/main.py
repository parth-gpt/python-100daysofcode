import requests
from datetime import datetime

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = "parthgpt"
TOKEN = {Token}

user_params = {
    "token": {Token},
    "username": "parthgpt",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)

GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

graph_params = {
    "id": "graph10",
    "name": "Push-up Graph",
    "unit": "push-ups",
    "type": "int",
    "color": "momiji"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=GRAPH_ENDPOINT, json=graph_params, headers=headers)
# print(response.text)

GRAPH_PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/graph10"

today = datetime.now()

graph_pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many push-ups did you do today?"),
}

response = requests.post(url=GRAPH_PIXEL_ENDPOINT, json=graph_pixel_params, headers=headers)
print(response.text)
