from user.Base_user import User
from datetime import datetime
from enum import StrEnum,auto
from workout.workoutplan import IndoreWorkout,OutdoorWorkout
from typing import Callable
from weather.weather import current_weather,save_weather_data

type workoutFun = Callable[[str],None]

class days(StrEnum):
    SUNDAY =auto()
    MONDAY =auto()
    TUESDAY =auto()
    WENESDAY = auto()
    THURSDAY = auto()
    FRIDAY = auto()
    SATAURDAY = auto()
class Planner(User):
    def __init__(self, name, age, height, weight, contactno, fitnesslevel,city):
        super().__init__(name, age, height, weight, contactno, fitnesslevel,city)
        self.day = datetime.today().strftime('%A')
        self.day = self.day.lower()

    def indoor_plan(self)->workoutFun:
        
        if self.day == str(days.SUNDAY):
           return IndoreWorkout.cardio(self.fitnesslevel)
        elif self.day == str(days.MONDAY):
            return IndoreWorkout.cardio(self.fitnesslevel)
        elif self.day== days.TUESDAY:
            return IndoreWorkout.cardio(self.fitnesslevel)
        elif self.day ==days.WENESDAY:
            return IndoreWorkout.weight()
        elif self.day ==days.THURSDAY:
            return IndoreWorkout.swimming()
        elif self.day == days.FRIDAY:
            return IndoreWorkout.cardio()
        
        else: print(f"Today is {days.SATAURDAY} its a rest day , take good rest drink water be healthy")
        

    def outdoor_plan(self):
        if self.day == days.SUNDAY:
           return OutdoorWorkout.running(self.fitnesslevel)
        elif self.day ==days.MONDAY:
            return OutdoorWorkout.running(self.fitnesslevel)
        elif self.day== days.TUESDAY:
            return OutdoorWorkout.running(self.fitnesslevel)
        elif self.day ==days.WENESDAY:
            return OutdoorWorkout.rockcliming()
        elif self.day ==days.THURSDAY:
            return OutdoorWorkout.Treaking()
        
        elif self.day == days.FRIDAY:
            return OutdoorWorkout.running()
        
        else:
            print(f"Today is {days.SATAURDAY} its a rest day , take good rest drink water be healthy")
        
