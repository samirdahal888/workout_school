from user.Base_user import User
from factory import factory
from datetime import datetime,date
from weather.weather import featch_weather_data,current_weather,save_weather_data
from config import BAD_WEATHER


def greet_user(user:User)->None:
    print(f'Hii {user.name} welcome to the workout school once again')
    print(f"Today is {date.today()} {datetime.today().strftime('%A')} ")

def weather_handeler(user:User)->None:
    if featch_weather_data(user.city) == False:
         return
    else:
        featch_weather_data(user.city)
        save_weather_data(user.city)
        weather_data = current_weather(user.city)
        #{
        #      'weather':'sunny',
        #      'description':"good weather",
        #      'city_name':'kathmandu'
        # }
        print('*********************** WEATHER *************************')
        print(f"It's {weather_data['weather'] } today  at {weather_data['city_name']} \nweather discription :{weather_data["description"]} ")

        if weather_data['weather'] in BAD_WEATHER :
                print("The weather is not so good today so lets do indoor workout")
                print()
                print('*************Your workout plan for today***************')
                user.indoor_plan()
                print('**********************************************')

        else:
            indoor_or_outdoor =  int(input("Do you want to do indoor or outdoor workout today\n press 1 for indoor \n press 2 for outdoor :"))

            if indoor_or_outdoor==1:
                print('*************Your workout plan for today***************')
                user.indoor_plan()
            else:
                print('*************Your workout plan for today***************')
                user.outdoor_plan()
        

def main()->None:
    print()
    print('*************** WORKOUT SCHOOL **************************')
    print()
    name = input("Enter your name:")
    print()
    user = factory.get_user_data(name)
    user.to_dict()
    user.ExporttoJSON()
    print()
    print('******************** WELCOME ************************')
    greet_user(user)
    print()
    weather_handeler(user)


if __name__ =='__main__':
    main()





