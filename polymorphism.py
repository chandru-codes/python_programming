#create a class called animal with a method sound() that prints "animal makes a sound"
#create a derived class called dog that inherits from animal and overrides the sound() method to print "dog barks".
#create another derived class called bird that inheris from animal and overrides the sound() method to print "Birds sing".
#Example for Polymorphism and Method Overriding.

class animal:
    def sound(self):
        print("animal makes a sound")

class dog(animal):
    def sound(self):
        print("dog barks")

class bird(animal):
    def sound(self):
        print("birds sing")

d1=dog()
d1.sound()

b1=bird()
b1.sound()

#create a base class called shape with a method area() that returns 0.
#create a derived class called rectangle that inherits from shape and overrides the area() method to calculate and return the area of the rectangle.

class shape:
    def area(self):
        return 0

class rectangle(shape):
    def area(self):
        l=10
        b=20
        rect_area=l*b
        print(rect_area)

r1=rectangle()
r1.area()

#create a base class called person with a constructor that takes a name as a parameter.
#create a derived class called student that inherits from person and has a constructor that takes a parameter called grade.
#write a method in student to display the name and grade of the student.
#use super keyword to achieve this.

class person():
    def __init__(self,name):
        self.name=name

class student(person):
    def __init__(self,name,grade):
        super().__init__(name)
        self.grade=grade

    def display(self):
        print("Name:",self.name)
        print("Grade:",self.grade)

s1=student("Chandru","A")
s1.display()

#create a base class called vehicle with a method start() that prints "vehicle started".
#create a derived class called car that inherits from vehicle and overrides the start() method to print "car started"

class vehicle:
    def start(self):
        print("vehicle started")

class car(vehicle):
    def start(self):
        print("car started")
        
v1=vehicle()
v1.start()

c1=car()
c1.start()

#create a base class employee with properties name and salary.
#create a derived class called manager that inherits from employee and adds a property "department".
#write a method in manager to display the name,salary and department of the manager.

class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

class manager(employee):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department=department
        

    def display(self):
        print("Name:",self.name)
        print("Salary:",self.salary)
        print("Department:",self.department)

m1=manager("Chandru","50000","IT")
m1.display()
    
