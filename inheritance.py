# single inheritance

class dad:
    
    def phone(self):
        print("Dad's phone")

class son(dad):

    def laptop(self):
        print("son's laptop")

ram=son()    # creating object for class son and accessing the function present in class dad.
ram.phone()

# multiple inheritance

class dad:
    
    def phone(self):
        print("Dad's phone")

class mom:
    def sweet(self):
        print("Mom's sweet")

class son(dad,mom):

    def laptop(self):
        print("son's laptop")

ram=son()
ram.phone()
ram.sweet()

# Multi-level inheritance

class grandpa:
    def phone(self):
        print("grandpa's phone")

class dad(grandpa):
    def money(self):
        print("Dad's money")

class son(dad):
    def laptop(self):
        print("Son's laptop")

ram=son()
ram.laptop()
ram.money()

ramesh=dad()
ramesh.phone()

ram.phone() # By using class son object(ram) we can access grandpa class.

# Hierarchy inheritance (multiple classes inherits a single class)

class dad:
    def money(self):
        print("Dad's money")

class son1(dad):
    pass  # pass is used to have a empty class.

class son2(dad):
    pass

class son3(dad):
    pass

s2=son2()
s2.money()

# Hybrid inheritance

class dad:
    def money(self):
        print("Dad's money")

class land:
    def important(self):
        print("Important land")

class son1(dad,land):
    pass  # pass is used to have a empty class.

class son2(dad):
    pass

class son3(dad):
    pass

s1=son1()
s1.money()
s1.important()
s2 = son2()
s2.money()












































