from enum import IntEnum

class SET_LEVEL(IntEnum):
    BASIC = 10
    INTERMEDIATE = 25
    ADVANCE = 50
    
class IndoreWorkout:

    @staticmethod
    def cardio(level:str)->None:
        """cardio workout for strength gain"""

        if level=='basic':
            print(f'{2*SET_LEVEL.BASIC} minute running')
            print(f'{2*SET_LEVEL.BASIC} minute streaching')
            print(f"pull ups {2*SET_LEVEL.BASIC} times ")
            print(f'push up {2*SET_LEVEL.BASIC} times')
        if level=='intermediate':
            print(f'{2*SET_LEVEL.INTERMEDIATE} minute warmup')
            print(f'{2*SET_LEVEL.INTERMEDIATE} minute streaching')
            print(f"pull ups {2*SET_LEVEL.INTERMEDIATE} times ")
            print(f'push up {2*SET_LEVEL.INTERMEDIATE} times')
        if level=='advance':
            print(f'{2*SET_LEVEL.INTERMEDIATE} minute running')
            print(f'{2*SET_LEVEL.INTERMEDIATE} minute streaching')
            print(f"pull ups {2*SET_LEVEL.INTERMEDIATE} times ")
            print(f'push up {2*SET_LEVEL.INTERMEDIATE} times')
    @staticmethod
    def swimming(level:str)->None:
        if level=='basic':
            print(f'{2*SET_LEVEL.BASIC} minute warmup')
            print(f'{2*SET_LEVEL.BASIC} minute slow swim')
            print(f"{2*SET_LEVEL.BASIC} mddium pase ")
            print(f'{2*SET_LEVEL.BASIC} faste')
        if level=='intermediate':
            print(f'{2*SET_LEVEL.INTERMEDIATE} minute running')
            print(f'{2*SET_LEVEL.INTERMEDIATE} minute streaching')
            print(f"pull ups {2*SET_LEVEL.INTERMEDIATE} times ")
            print(f'push up {2*SET_LEVEL.INTERMEDIATE} times')
        if level=='advance':
            print(f'{2*SET_LEVEL.ADVANCE} minute running')
            print(f'{2*SET_LEVEL.ADVANCE} minute streaching')
            print(f"pull ups {2*SET_LEVEL.ADVANCE} times ")
            print(f'push up {2*SET_LEVEL.ADVANCE} times')


class OutdoorWorkout:
    @staticmethod
    def running(level:str)->None:
        if level =='basic':
            print(f'{SET_LEVEL.BASIC} km running')

        if level =='Intermediate':
            print(f"{SET_LEVEL.INTERMEDIATE} km running")


        if level =='Advance':
            print(f"{SET_LEVEL.ADVANCE} km running")


          



    

