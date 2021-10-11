import requests
from datetime import datetime

GENDER = "male"
WEIGHT_KG = 65
HEIGHT_CM = 179
AGE = 18

APP_ID = {APP_ID}
API_KEY = "977ba1e2c88ea8bdaa9bcacc299689b5"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

today = datetime.now()

params = {
    "query": input("Tell me which exercise you did? "),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

response = requests.post(EXERCISE_ENDPOINT, json=params, headers=headers)
result = response.json()

SHEET_ENDPOINT = "https://api.sheety.co/8aacc08837318b5888b10e9f15a80d1a/myWorkouts/workouts"

info_params = {
    "workout": {
        "date": today.strftime("%d/%m/%Y"),
        "time": today.strftime("%X"),
        "exercise": result["exercises"][0]["name"].title(),
        "duration": result["exercises"][0]["duration_min"],
        "calories": result["exercises"][0]["nf_calories"],
    }
}

sheet_headers = {
    "Authorization": "Bearer {Author}",
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}
sheet_response = requests.post(SHEET_ENDPOINT, json=info_params, headers=sheet_headers)

