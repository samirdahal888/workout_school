import os
from pathlib import Path
import requests
from datetime import date
import json
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv('WEATHER_API_KEY')


def current_weather(city:str,filepath:Path)->None:
    
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}')
    data = response.json()
    print(data)
    weather_data = {
        'weather':data['weather'][0]['main'],
        'description':data['weather'][0]['description'],   
    }
    with open(f'{filepath}/{date.today()}_{city}.json','w') as f:
        json.dump(weather_data,f,indent=4)

current_weather('kathmandu',filepath='/home/samir-dahal/wokout_school/data/weather_data')