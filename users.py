class USER:
    """base class for user

    name: name of the user
    age:age of the user
    height:height of the user
    weight:weight of the user
    contactno:contact no of the user
    fitnesslevel: fitness level of user (basic intermidiate advance)
    
    
    
    """

    def __init__(self,name:str,age:int,height:int,weight:int,contactno:str,fitnesslevel:str,)->None:
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.contactno = contactno
        self.fitnesslevel = fitnesslevel
        

    

        