import os
from pathlib import Path
import requests
from datetime import date
import json
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv('WEATHER_API_KEY')


def featch_weather_data(city:str)->json:
    """it helps to featch the weather of the particular city based on the city provided and correct API"""
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}')
    data = response.json()
    return data
   
def current_weather(city:str)->None:
    """helps to get the weateher conditon and its description"""

    data = featch_weather_data(city)
    weather_data = {
        'weather':data['weather'][0]['main'],
        'description':data['weather'][0]['description'],   
        'city_name':data['name']
    }
    return weather_data


def save_weather_data(filepath:Path,city)->None:
    weather_data = featch_weather_data(city)
    with open(f'{filepath}/{date.today()}_{city}.json','w') as f:
        json.dump(weather_data,f,indent=4)




