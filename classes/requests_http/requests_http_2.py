# Есть API по информации о супергероях с информацией по всем супергероям.
#
# Напишите функцию для определения самого умного супергероя среди Hulk, Captain America, Thanos.

import os
import time

import requests
from dotenv import load_dotenv

load_dotenv('../../.env')

url = os.getenv('URL_SUPERHERO_API')

def get_the_smartest_superhero(superheros):
   the_smartest_superhero = ''
   max_intelligence = 0
   for superhero in superheros:
       response = requests.get(f"{url}/id/{superhero}.json")
       hero = response.json()
       if hero['powerstats']['intelligence'] > max_intelligence:
           max_intelligence = hero['powerstats']['intelligence']
           the_smartest_superhero = hero['name']

   return the_smartest_superhero

if __name__ == '__main__':
    hulk = 332
    captain_america = 149
    thanos = 655
    id_hero = (hulk, captain_america, thanos)

    print(get_the_smartest_superhero(id_hero))
