from enum import IntEnum
from logger.logger import get_logger
import logging

class SET_LEVEL(IntEnum):
    BASIC = 10
    INTERMEDIATE = 25
    ADVANCE = 50

logger = get_logger(__name__,logging.DEBUG)
def cardio(level:str)->None:
    """cardio workout for strength gain"""
    print("**Today lets do cardio**")


    if level=='basic':
        print(f'{SET_LEVEL.BASIC} minute running')
        print(f'{SET_LEVEL.BASIC} minute streaching')
        print(f"pull ups {SET_LEVEL.BASIC} times ")
        print(f'push up {SET_LEVEL.BASIC} times')
    elif level=='intermediate':
        print(f'{SET_LEVEL.INTERMEDIATE} minute warmup')
        print(f'{SET_LEVEL.INTERMEDIATE} minute streaching')
        print(f"pull ups {SET_LEVEL.INTERMEDIATE} times ")
        print(f'push up {SET_LEVEL.INTERMEDIATE} times')
    elif level=='advance':
        print(f'{SET_LEVEL.INTERMEDIATE} minute running')
        print(f'{SET_LEVEL.INTERMEDIATE} minute streaching')
        print(f"pull ups {SET_LEVEL.INTERMEDIATE} times ")
        print(f'push up {SET_LEVEL.INTERMEDIATE} times')

    else:
        print("Invalid level. Choose from: basic, intermediate, advance.")

def swimming(level:str)->None:
    logger.debug(f"level getting is {level} level")
    print("**Today lets do SWIMMING**")

    if level=='basic':
        print(f'{SET_LEVEL.BASIC} minute warmup')
        print(f'{SET_LEVEL.BASIC} minute slow swim')
        print(f"{SET_LEVEL.BASIC}laps mddium pase ")
        print(f'{SET_LEVEL.BASIC} laps faste')
    elif level=='intermediate':
        print(f'{SET_LEVEL.INTERMEDIATE} minute warmup')
        print(f'{SET_LEVEL.INTERMEDIATE} minute slow swim')
        print(f"{SET_LEVEL.INTERMEDIATE}laps mddium pase ")
        print(f'{SET_LEVEL.INTERMEDIATE} laps faste')
    elif level=='advance':
        print(f'{SET_LEVEL.ADVANCE} minute warmup')
        print(f'{SET_LEVEL.ADVANCE} minute slow swim')
        print(f"{SET_LEVEL.ADVANCE}laps mddium pase ")
        print(f'{SET_LEVEL.ADVANCE} laps faste')
    else:
        print("Invalid level. Choose from: basic, intermediate, advance.")

def weight(level:str)->None:
    print("**Today lets do weight**")

    if level == 'basic':
        print(f'{SET_LEVEL.BASIC} minute warmup')
        print(f'{SET_LEVEL.BASIC} reps of lightweight exercises')
        print(f"{SET_LEVEL.BASIC} reps of bodyweight exercises")
        print(f'{SET_LEVEL.BASIC} reps of stretching')
    elif level == 'intermediate':
        print(f'{SET_LEVEL.INTERMEDIATE} minute warmup')
        print(f'{SET_LEVEL.INTERMEDIATE} reps of moderate weight exercises')
        print(f"{SET_LEVEL.INTERMEDIATE} reps of bodyweight + resistance band")
        print(f'{SET_LEVEL.INTERMEDIATE} reps of stretching and mobility')
    elif level == 'advance':
        print(f'{SET_LEVEL.ADVANCE} minute warmup')
        print(f'{SET_LEVEL.ADVANCE} reps of heavy weight training')
        print(f"{SET_LEVEL.ADVANCE} reps of bodyweight + added weight")
        print(f'{SET_LEVEL.ADVANCE} reps of advanced mobility & stretching')
    else:
        print("Invalid level. Choose from: basic, intermediate, advance.")
