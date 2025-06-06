from user.Base_user import User
from datetime import datetime
from enum import StrEnum,auto
from workout.indoor import cardio,swimming,weight
from workout.outdoor import running,hike,rockcliming,cycling
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

day = datetime.today().strftime('%A')
day = day.lower()
logger.debug(f"Today is {day}")

class Planner(User):

    ''' class the helps to plan for the workout , indoor or outdoor'''

    def indoor_plan(self)->workoutFun:
        '''indoor workout plan for users for day basis '''
        #cardio ,swimming , weight
        logger.debug(f"Today is {day} and starting the workout plan for today")
        logger.debug(f'fiteness level {self.fitnesslevel}')
        
        if day == str(days.SUNDAY):
           return cardio(self.fitnesslevel)
        elif day == str(days.MONDAY):
            return swimming(self.fitnesslevel)
        elif day== days.TUESDAY:
            return cardio(self.fitnesslevel)
        elif day ==days.WEDNESDAY:
            return weight(self.fitnesslevel)
        elif day ==days.THURSDAY:
            return weight(self.fitnesslevel)
        elif day == days.FRIDAY:
            return swimming(self.fitnesslevel)
        
        else: print(f"Today is {days.SATAURDAY} its a rest day , take good rest drink water be healthy")
        

    def outdoor_plan(self)->workoutFun:
        '''outdoor workout plan for users for day basis '''

        logger.debug(f"Today is {day} and starting the workout plan for today")

        
        if day == days.SUNDAY:
           return running(self.fitnesslevel)
        elif day ==days.MONDAY:
            return hike(self.fitnesslevel)
        elif day== days.TUESDAY:
            return cycling(self.fitnesslevel)
        elif day ==days.WEDNESDAY:
            return rockcliming(self.fitnesslevel)
        elif day ==days.THURSDAY:
            return running(self.fitnesslevel)
        
        elif day == days.FRIDAY:
            return cycling(self.fitnesslevel)
        
        else:
            print(f"Today is {days.SATAURDAY} its a rest day , take good rest drink water be healthy")
        
