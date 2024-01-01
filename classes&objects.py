#Create a class called student.
#create a variable => name and register number using constructor.
#create a function called display which should display the name and register number of the student.


class student:
    def __init__(self):
        self.name=""
        self.reg_no=""

    def display(self):
        print("Name:",self.name)
        print("Register Number:",self.reg_no)

s1=student()
s2=student()

s1.name="Chandru"
s1.reg_no="03"

s2.name="Parth"
s2.reg_no="12"

s1.display()
s2.display()

#create a class called fruit.
#create a variable called color using __init__ method
#create a object called apple"Pass the color variable as a parameter through object".

class fruit:
    def __init__(self,col):
         self.color=col
         
apple=fruit("red")
print(apple.color)

#create a class called teacher.
#create a variable => name & register number using constructor.
#create a function called display which should display the name & register number of the teacher.
#create t1 & t2 object and pass the name & reg no value through object.

class teacher:
    def __init__(self,name,reg):
        self.name=name
        self.regno=reg

    def display(self):
        print("Name:",self.name)
        print("Register no:",self.regno)

t1=teacher("Chandru","3")
t2=teacher("Parth","12")

t1.display()
t2.display()

#create a class called calculator.
#create a variable called a and b.
#create a function called add,sub,mul,div & all functions should take 2 variables as parameter.
#pass the a and b value through object().

class calculator:
    def __init__(self,a,b):
        self.num1=a
        self.num2=b
        
    def add(self):
        print("Add:",self.num1+self.num2)

    def sub(self):
        print("Sub:",self.num1-self.num2)

    def mul(self):
        print("Mul:",self.num1*self.num2)

    def div(self):
        print("Div:",self.num1/self.num2)
          

obj1=calculator(10,2)
obj1.add()

obj2=calculator(10,2)
obj2.sub()

obj3=calculator(10,2)
obj3.mul()

obj4=calculator(10,2)
obj4.div()
       

# create a class called laptop and create a following variables & functions.
# variables=> price, processor, ram
# create object=> HP, DELL, LENOVO
# Then print the all the variables for each object.

class laptop:
    price=int()
    proc=""
    ram=""

hp=laptop()
dell=laptop()
lenovo=laptop()

hp.price=50000
hp.proc="i5"
hp.ram="8GB"

dell.price=65000
dell.proc="i7"
dell.ram="16GB"

lenovo.price=80000
lenovo.proc="i9"
lenovo.ram="32GB"

print("HP LAPTOP")
print("Price:",hp.price)
print("Processor:",hp.proc)
print("Ram:",hp.ram)

print("DELL LAPTOP")
print("Price:",dell.price)
print("Processor:",dell.proc)
print("Ram:",dell.ram)

print("LENOVO LAPTOP")
print("Price:",lenovo.price)
print("Processor:",lenovo.proc)
print("Ram:",lenovo.ram)


    
        






































    
