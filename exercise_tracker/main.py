import os
import requests
import datetime

APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]
NUTRI_URL = os.environ["NUTRI_URL"]
SHEETY_URL = os.environ["SHEETY_URL"]
AUTH_TOKEN = os.environ["AUTH_TOKEN"]

WEIGHT = 52
HEIGHT = 173
AGE = 19

DATE = datetime.date.today().strftime("%d/%m/%Y")
TIME = datetime.datetime.now().time().strftime("%H:%M")

nutri_params = {
    "query": str(input("Tell me which exercise you did: ")),
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}
nutri_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}
nutri_response = requests.post(NUTRI_URL, json=nutri_params, headers=nutri_headers)
nutri_response.raise_for_status()
data = nutri_response.json()
exercises_data = data["exercises"]

headers = {
    "Authorization": AUTH_TOKEN
}
for exercise in exercises_data:
    params = {"workout": {
        "date": DATE,
        "time": TIME,
        "exercise": exercise["user_input"].title(),
        "duration": exercise["duration_min"],
        "calories": exercise["nf_calories"]
    }
    }
    sheety_response = requests.post(SHEETY_URL, json=params, headers=headers)
    sheety_response.raise_for_status()
    print(sheety_response.text)
