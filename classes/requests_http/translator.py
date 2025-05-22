import os

import requests
from dotenv import load_dotenv

load_dotenv("../../.env")
from pprint import pprint

url = os.getenv("URL_TRANSLATE")
token = os.getenv("API_KEY_Y_TRANS")


def translate_word(word):
    params = {"key": token, "text": word, "lang": "ru-en"}
    response = requests.get(url, params=params)
    trans_word = response.json()["def"][0]["tr"][0]["text"]

    return trans_word


if __name__ == "__main__":
    word = "машина"
    assert translate_word(word) == "car"
