class Animal:
    
    def __init__(self, name, type, owner):
        self.__name = name
        self.type = type
        self.owner = owner
        
    
    def __str__(self):
        return f'Your animal is a {self.type} and it\'s name is {self.__name}'
    
    def bark(self):
        return 'Bark Bark'
    
    
    
    
class Owner:
    
    def __init__(self, name, address, phone_number):
        self.__name = name
        self.__address = address
        self.__number = phone_number
        
        
    @property
    def email(self):
        return self.__name
    


owner1 = Owner('James', '620 John Paul Jones', '111-222-3333')
owner2 = Owner('Smith', '1213 Smith Drive', '444-222-3232')


dog = Animal("Mike", 'Dog', owner=owner1) 



print(owner1.email)
    