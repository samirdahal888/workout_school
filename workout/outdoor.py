from workout.indoor import SET_LEVEL

def running(level:str)->None:
    '''Running workout plan for users based on there fitnesslevel'''
    print("lest do the following workout today")
    if level =='basic':
        print(f'{SET_LEVEL.BASIC} km running')
    elif level =='intermediate':
        print(f"{SET_LEVEL.INTERMEDIATE} km running")
    elif level =='advance':
        print(f"{SET_LEVEL.ADVANCE} km running")
    else:
        print("Invalid level. Choose from: basic, intermediate, advance.")
def cycling(level:str)->None:
    '''cycling workout plan for users based on there fitnesslevel'''
    print("lest do the following workout today")

    if level=='basic':
        print(f"{SET_LEVEL.BASIC} km cycling")

    elif level=="intermediate":
        print(f"{SET_LEVEL.INTERMEDIATE} km cycling")
    elif level =='advance':
        print(f"{SET_LEVEL.ADVANCE} km cycling")
    else:
        print("Invalid level. Choose from: basic, intermediate, advance.")



def hike(level:str)->None:
    ''' hike workout plan for users based on there fitnesslevel'''
    print("lest do the following workout today")

    if level=='basic':
        print(f"{SET_LEVEL.BASIC} km hiking")

    elif level=="intermediate":
        print(f"{SET_LEVEL.INTERMEDIATE} km hiking")
    elif level =='advance':
        print(f"{SET_LEVEL.ADVANCE} km hiking")
    else:
        print("Invalid level. Choose from: basic, intermediate, advance.")


def rockcliming(level:str)->None:
    ''' rockcliming workout plan for users based on there fitnesslevel'''
    print("lest do the following workout today")


    if level=='basic':
        print(f"{SET_LEVEL.BASIC} minute rockcliming")

    elif level=="intermediate":
        print(f"{SET_LEVEL.INTERMEDIATE} minute rockcliming")
    elif level =='advance':
        print(f"{SET_LEVEL.ADVANCE} minute rockcliming")
    else:
        print("Invalid level. Choose from: basic, intermediate, advance.")





    
