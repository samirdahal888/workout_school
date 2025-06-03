import os
from pathlib import Path
import requests
from datetime import date
import json
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv('WEATHER_API_KEY')


def featch_weather_data(city)->json:
    """it helps to featch the weather of the particular city based on the city provided and correct API"""
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}')
    data = response.json()
    return data


    
def current_weather(city:str,filepath:Path)->dict:
    """helps to get the weateher conditon and its description"""

    data = featch_weather_data(city)
    weather_data = {
        'weather':data['weather'][0]['main'],
        'description':data['weather'][0]['description'],   
    }
    with open(f'{filepath}/{date.today()}_{city}.json','w') as f:
        json.dump(weather_data,f,indent=4)

    return weather_data

# current_weather('kathmandu',filepath='/home/samir-dahal/wokout_school/data/weather_data')