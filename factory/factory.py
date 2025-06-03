from user.User_workout_Planner import Planner
from pathlib import Path
import json

def form()->Planner:
    name = input("Enter your name:")
    age = int(input("Enter your age:"))
    height = float(input("Enter you height:"))
    weight = float(input("Enter your weight:"))
    contact = input("Enter contact no:")
    fitnesslevel = input("Enter your fitnesslevel:")
    city = input('Enter city:')

    return Planner(name,age,height,weight,contact,fitnesslevel,city)

def get_user_data(Base_path:Path,username:str)->Planner:
    '''get user data from file if exist , if not then creater user'''
    try:
        base_file = Base_path
        target_file = f"{username}.json"
        json_file = list(base_file.rglob(target_file))

        if json_file:
            file_path = json_file[0]
            with open(file_path,'r') as f:
                user_data = json.load(f)
        return Planner(user_data['name'],user_data["age"],user_data['height'],user_data['weight'],user_data["contact"],user_data['fitnesslevel'],user_data['city'])

    except Exception:
        print('you are the new member here so please enter your details')
        return form()
