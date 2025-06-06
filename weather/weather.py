import os
from pathlib import Path
import requests
from datetime import date
import json
from dotenv import load_dotenv
from logger.logger import get_logger
import logging
logger = get_logger(__name__,logging.DEBUG)
load_dotenv()

API_KEY = os.getenv('WEATHER_API_KEY')



def featch_weather_data(city:str)->json:
    """It helps to featch the weather of the particular city based on the city provided and correct API"""
    logger.info("starting the featch_weather_data function to featch data from api")
    
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}')
    logger.debug(f"respose status code from api is {response.status_code}")
    if response.status_code!=200:
        logger.debug(f"city not found {response.status_code}")
        print('city not found')
        return False
    data = response.json()
    return data
   
def current_weather(city:str)->None:
    """helps to get the weateher conditon and its description"""
    logger.info('current weather function started ')

    data = featch_weather_data(city)
    weather_data = {
        'weather':data['weather'][0]['main'],
        'description':data['weather'][0]['description'],   
        'city_name':data['name']
    }
    return weather_data


def save_weather_data(city)->None:
    logger.info(f'saving the weather of {city} data to weather_data')
    weather_data = featch_weather_data(city)
    os.makedirs("data/weather_data",exist_ok=True)

    with open(f'data/weather_data/{date.today()}_{city}.json','w') as f:
        json.dump(weather_data,f,indent=4)




