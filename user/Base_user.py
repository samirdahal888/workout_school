import json
from pathlib import Path
import os
from abc import ABC,abstractmethod

class User(ABC):
    """base class for user

    name: name of the user
    age:age of the user
    height:height of the user
    weight:weight of the user
    contactno:contact no of the user
    fitnesslevel: fitness level of user (basic intermidiate advance)
    
    
    
    """

    def __init__(self,name:str,age:int,height:int,weight:int,contactno:str,fitnesslevel:str,city:str)->None:
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.contactno = contactno
        self.fitnesslevel = fitnesslevel
        self.city = city
    @abstractmethod
    def indoor_plan(self):
        pass

    @abstractmethod
    def outdoor_plan(self):
        pass

    def to_dict(self)->dict:
        '''makes dictionary of the information provided'''
        dictionaty = {
            "name":self.name,
            "age":self.age,
            "height":self.height,
            "weight":self.weight,
            "contact":self.contactno,
            "fitnesslevel":self.fitnesslevel,
            'city':self.city

        }
        return dictionaty

    def ExporttoJSON(self,filepath:Path)->None:
        '''Export the dictionary to the json file in the desier file'''
        os.makedirs(filepath,exist_ok=True)
        json_file = f'{filepath}/{self.name}.json'
        
        with open(json_file,'w') as f:
            json.dump(self.to_dict(),f,indent=2)

    




    

        