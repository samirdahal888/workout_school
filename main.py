from user.User_workout_Planner import Basic
# self,name:str,age:int,height:int,weight:int,contactno:str,fitnesslevel:str,city:str
# name = input("Enter your name:")
# age = int(input("Enter your age:"))
# height = float(input("Enter you height:"))
# weight = float(input("Enter your weight:"))
# contact = input("Enter contact no:")
# fitnesslevel = input("Enter your fitnesslevel:")
# city = input('Enter city')


name = 'samir'

age =  12
height =5.5
weight = 44
contact = '9999999'
fitnesslevel = 'basic'
city ='kathmandu'


user  = Basic(name,age,height,weight,contact,fitnesslevel,city)
user.to_dict()
user.ExporttoJSON('/home/samir-dahal/wokout_school/data/user_data')
user.outdoor_plan()






