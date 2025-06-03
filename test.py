from weather.weather import featch_weather_data,save_weather_data,current_weather
from pathlib import Path
featch_weather_data('kathmandu')
save_weather_data(Path('/home/samir-dahal/wokout_school/data/weather_data'),'kathmandu')
weather_data = current_weather('kathmandu')
print(f"Hii , its {weather_data['weather'] } today  at {weather_data['city_name']} \n weather discription :{weather_data["description"]} ")

# get_user_data(Path('/home/samir-dahal/wokout_school/data'),'samir')