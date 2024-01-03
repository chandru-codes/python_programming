#Encapsulation
#The company name can't able to change
'''class company:
    def __init__(self):
        self.__companyname="Google"

    def display(self):
        print(self.__companyname) ##using private variable.


c1=company()
c1.display()
print(c1.self__companyname)''' # private variables can't be accessible outside of the class.
        
    
#using protected variable

class company:
    def __init__(self):
        self._companyname="Google"
        
class info(company):
    def display(self):
        print(self._companyname) #using protected variable.


i1=info()
i1.display() # protected variable can be accessed in derived class.

