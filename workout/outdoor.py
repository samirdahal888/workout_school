from workout.indoor import SET_LEVEL

def running(level:str)->None:
    if level =='basic':
        print(f'{SET_LEVEL.BASIC} km running')

    if level =='Intermediate':
        print(f"{SET_LEVEL.INTERMEDIATE} km running")


    if level =='Advance':
        print(f"{SET_LEVEL.ADVANCE} km running")
