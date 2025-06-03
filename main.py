from user.User_workout_Planner import Planner
from pathlib import Path
import json
from factory import factory
from datetime import datetime,date
from weather.weather import featch_weather_data,current_weather,save_weather_data


def main():
    name = input("Enter your name:")
    user = factory.get_user_data('/home/samir-dahal/wokout_school/data',name)
    user.to_dict()
    user.ExporttoJSON('/home/samir-dahal/wokout_school/data/user_data')
    print(f'Hii {name} welccome to the workout school once again')
    print(f"Today is {date.today()} {datetime.today().strftime('%A')} ")
    featch_weather_data(user.city)
    save_weather_data('/home/samir-dahal/wokout_school/data/weather_data',user.city)
    weather_data = current_weather(user.city
                                   )
    print(f"Hii , its {weather_data['weather'] } today  at {weather_data['city_name']} \n weather discription :{weather_data["description"]} ")

    bad_weather = ['Clouds','Rain','Wind']
    if weather_data['weather'] in bad_weather :
        print("The weather is not so good today so lets do indoor workout")
        user.indoor_plan()
    else:
        indoor_or_outdoor =  int(input("Do you want to do indoor or outdoor workout today\n press 1 for indoor \n press 2 for outdoor :"))
        if indoor_or_outdoor==1:
            user.indoor_plan()
        else:
            user.outdoor_plan()






    
    

    

if __name__ =='__main__':
    main()





