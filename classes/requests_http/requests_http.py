# Есть API по информации о супергероях с информацией по всем супергероям.
#
# Напишите функцию для определения самого умного супергероя среди Hulk, Captain America, Thanos.
import os

import requests
from dotenv import load_dotenv

load_dotenv('../../.env')

url = os.getenv('URL_SUPERHERO_API')


def get_the_smartest_superhero() -> str:
    the_smartest_superhero = ''
    name_heroes = ['Hulk', 'Captain America', 'Thanos']
    max_intelligence = 0
    response = requests.get(f'{url}/all.json')
    # with open(f'heros.json', 'w') as file:
    #     file.write(response.text)
    heroes = response.json()
    for hero in heroes:
        if hero['powerstats']['intelligence'] > max_intelligence and hero['name'] in name_heroes:
            max_intelligence = hero['powerstats']['intelligence']
            the_smartest_superhero = hero['name']

    return the_smartest_superhero


if __name__ == '__main__':
    print(get_the_smartest_superhero())
