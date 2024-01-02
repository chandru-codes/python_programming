class a:
    def __init__(self):
        print("A")

    def display(self):
        print("You are in class a")

class b():
    def __init__(self):
        super().__init__()
        print("B")

    def display(self):
        print("You are in class b")

class c(b,a): # left argument is taken in multiple inheritance.
    def __init__(self):
        super().__init__()
        print("c")
        

    def display(self):
        print("You are in class b")

obj2=c()
    
        
