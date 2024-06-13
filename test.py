import requests

url = "http://158.160.83.201:5444/predict_price"

params_list = [
    {"floor": 1, "rooms": 2, "studio": "true", "area": 50.0, "renovation": 1},
    {"floor": 2, "rooms": 3, "studio": "false", "area": 70.0, "renovation": 0},
    {"floor": 3, "rooms": 1, "studio": "true", "area": 40.0, "renovation": 1},
    {"floor": 4, "rooms": 2, "studio": "false", "area": 60.0, "renovation": 0},
    {"floor": 5, "rooms": 3, "studio": "true", "area": 80.0, "renovation": 1},
    {"floor": 6, "rooms": 1, "studio": "false", "area": 30.0, "renovation": 0},
    {"floor": 7, "rooms": 2, "studio": "true", "area": 55.0, "renovation": 1},
    {"floor": 8, "rooms": 3, "studio": "false", "area": 75.0, "renovation": 0},
    {"floor": 9, "rooms": 1, "studio": "true", "area": 35.0, "renovation": 1},
    {"floor": 10, "rooms": 2, "studio": "false", "area": 65.0, "renovation": 0},
]

for i, params in enumerate(params_list):
    response = requests.get(url, params=params)
    print(f"Request {i+1} with params {params}")
    print(f"Response: {response.text}\n")

