from enum import IntEnum

class SET_LEVEL(IntEnum):
    BASIC = 10
    INTERMEDIATE = 25
    ADVANCE = 50
    
class workout:

    @staticmethod
    def cardio(level):
        level = level.lower()
        if level=='basic':
            print(f'{2*SET_LEVEL.BASIC} minute running')
            print(f'{2*SET_LEVEL.BASIC} minute streaching')
            print(f"pull ups {2*SET_LEVEL.BASIC} times ")
            print(f'push up {2*SET_LEVEL.BASIC} times')
        if level=='basic':
            print(f'{2*SET_LEVEL.BASIC} minute running')
            print(f'{2*SET_LEVEL.BASIC} minute streaching')
            print(f"pull ups {2*SET_LEVEL.BASIC} times ")
            print(f'push up {2*SET_LEVEL.BASIC} times')

class intermediate_workout:
    def cardio():
        print('10min running')
        print('streaching')
        print("pull ups 30 times ")
        print('push up 50 times')

class advance_workout:
    def cardio():
        print('10min running')
        print('streaching')
        print("pull ups 30 times ")
        print('push up 50 times')
