import os
import time

import requests
from dotenv import load_dotenv

load_dotenv("../../.env")

url = os.getenv("URL_GEOCODE")
api_key = os.getenv("API_KEY_GEOCODE")


def find_uk_city(coordinates: list) -> str:
    uk_cities = [
        "Leeds",
        "London",
        "Liverpool",
        "Manchester",
        "Oxford",
        "Edinburgh",
        "Norwich",
        "York",
    ]
    for coordinate in coordinates:
        response = requests.get(
            f"{url}?lat={coordinate[0]}&lon={coordinate[1]}&api_key={api_key}"
        ).json()
        city = response["address"]["city"]
        if city in uk_cities:
            return city
        time.sleep(10)


if __name__ == "__main__":
    _coordinates = [
        ("55.7514952", "37.618153095505875"),
        ("52.3727598", "4.8936041"),
        ("53.4071991", "-2.99168"),
    ]
    assert find_uk_city(_coordinates) == "Liverpool"
