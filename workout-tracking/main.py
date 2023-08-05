import requests
from datetime import datetime as dt
import os

today = dt.now()
date = today.strftime("%d/%m/%Y")
time = today.strftime("%X")

GENDER = "female"
WEIGHT = 53.90
HEIGHT = 162.56
AGE = 26

APP_ID = os.environ["NT_APP_ID"]
API_KEY = os.environ["NT_API_KEU"]
TOKEN = os.environ["NT_TOKEN"]

EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEET_ENDPOINT = os.environ["NT_SHEET_ENDPOINT"]

exercise_text = input("What exercise did you do?:")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

bearer_headers = {
    "Autherization": f"Bearer {TOKEN}"
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

response = requests.post(url=EXERCISE_ENDPOINT, json=parameters, headers=headers)
results = response.json()


for exercise in results["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }


row_response = requests.post(url=sheet_endpoint, json=SHEET_ENDPOINT, headers=bearer_headers)

print(row_response.text)
