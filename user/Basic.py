from user.users import User
from datetime import datetime
from enum import StrEnum,auto
from .workoutplan import workout
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

    def indoor_plan(self,level:str)->workoutFun:
        
        if self.day == str(days.SUNDAY):
           return workout.cardio(level)
        elif self.day == str(days.MONDAY):
            return workout.cardio('basic')
        elif self.day== days.TUESDAY:
            return workout.swimming()
        elif self.day ==days.WENESDAY:
            return workout.weight()
        elif self.day ==days.THURSDAY:
            return workout.swimming()
        
        elif self.day == days.FRIDAY:
            return self.cardio()
        
        else: print(f"Today is {days.SATAURDAY} its a rest day , take good rest drink water be healthy")
        

        

        # swimming
        # cardio
        # weight


        pass
    def outdoor_plan(self):

        if self.day == days.SUNDAY:
           return running()
        elif self.day ==days.MONDAY:
            return hiking()
        elif self.day== days.TUESDAY:
            return cycling()
        elif self.day ==days.WENESDAY:
            return rockcliming()
        elif self.day ==days.THURSDAY:
            return Treaking()
        
        elif self.day == days.FRIDAY:
            return running()
        
        else:
            print(f"Today is {days.SATAURDAY} its a rest day , take good rest drink water be healthy")
        
        
        #running
        #hiking
        #cycling
        #rockcliming
        #Treaking
    