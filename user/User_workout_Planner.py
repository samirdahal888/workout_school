from user.Base_user import User
from datetime import datetime
from enum import StrEnum,auto
from workout.indoor import cardio,swimming
from workout.outdoor import running
from typing import Callable
import logging
from logger.logger import get_logger
logger = get_logger(__name__,logging.DEBUG)

type workoutFun = Callable[[str],None]

class days(StrEnum):
    SUNDAY =auto()
    MONDAY =auto()
    TUESDAY =auto()
    WEDNESDAY = auto()
    THURSDAY = auto()
    FRIDAY = auto()
    SATAURDAY = auto()
class Planner(User):
    def __init__(self, name, age, height, weight, contactno, fitnesslevel,city):
        super().__init__(name, age, height, weight, contactno, fitnesslevel,city)
        self.day = datetime.today().strftime('%A')
        self.day = self.day.lower()
        logger.debug(f"Today is {self.day}")

    def indoor_plan(self)->workoutFun:
        #cardio ,swimming , weight
        logger.debug(f"Today is {self.day} and starting the workout plan for today")
        
        if self.day == str(days.SUNDAY):
           return cardio(self.fitnesslevel)
        elif self.day == str(days.MONDAY):
            return cardio(self.fitnesslevel)
        elif self.day== days.TUESDAY:
            return cardio(self.fitnesslevel)
        elif self.day ==days.WEDNESDAY:
            return cardio(self.fitnesslevel)
        elif self.day ==days.THURSDAY:
            return wimming()
        elif self.day == days.FRIDAY:
            return cardio()
        
        else: print(f"Today is {days.SATAURDAY} its a rest day , take good rest drink water be healthy")
        

    def outdoor_plan(self):
        logger.debug(f"Today is {self.day} and starting the workout plan for today")

        
        if self.day == days.SUNDAY:
           return OutdoorWorkout.running(self.fitnesslevel)
        elif self.day ==days.MONDAY:
            return OutdoorWorkout.running(self.fitnesslevel)
        elif self.day== days.TUESDAY:
            return OutdoorWorkout.running(self.fitnesslevel)
        elif self.day ==days.WEDNESDAY:
            return OutdoorWorkout.rockcliming()
        elif self.day ==days.THURSDAY:
            return OutdoorWorkout.Treaking()
        
        elif self.day == days.FRIDAY:
            return OutdoorWorkout.running()
        
        else:
            print(f"Today is {days.SATAURDAY} its a rest day , take good rest drink water be healthy")
        
