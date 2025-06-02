from user.users import User
from datetime import datetime
from enum import StrEnum,auto
from .workoutplan import IndoreWorkout,OutdoorWorkout
from typing import Callable

type workoutFun = Callable[[str],None]

class days(StrEnum):
    SUNDAY =auto()
    MONDAY =auto()
    TUESDAY =auto()
    WENESDAY = auto()
    THURSDAY = auto()
    FRIDAY = auto()
    SATAURDAY = auto()
class Basic(User):
    def __init__(self, name, age, height, weight, contactno, fitnesslevel):
        super().__init__(name, age, height, weight, contactno, fitnesslevel)
        self.day = datetime.today().strftime('%A')
        self.day = self.day.lower()

    def indoor_plan(self)->workoutFun:
        
        if self.day == str(days.SUNDAY):
           return IndoreWorkout.cardio(self.fitnesslevel)
        elif self.day == str(days.MONDAY):
            return IndoreWorkout.cardio(self.fitnesslevel)
        elif self.day== days.TUESDAY:
            return IndoreWorkout.swimming()
        elif self.day ==days.WENESDAY:
            return IndoreWorkout.weight()
        elif self.day ==days.THURSDAY:
            return IndoreWorkout.swimming()
        elif self.day == days.FRIDAY:
            return IndoreWorkout.cardio()
        
        else: print(f"Today is {days.SATAURDAY} its a rest day , take good rest drink water be healthy")
        

    def outdoor_plan(self):

        if self.day == days.SUNDAY:
           return OutdoorWorkout.running()
        elif self.day ==days.MONDAY:
            return OutdoorWorkout.hiking()
        elif self.day== days.TUESDAY:
            return OutdoorWorkout.cycling()
        elif self.day ==days.WENESDAY:
            return OutdoorWorkout.rockcliming()
        elif self.day ==days.THURSDAY:
            return OutdoorWorkout.Treaking()
        
        elif self.day == days.FRIDAY:
            return OutdoorWorkout.running()
        
        else:
            print(f"Today is {days.SATAURDAY} its a rest day , take good rest drink water be healthy")
        
