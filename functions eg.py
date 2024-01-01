#create a function called called add(),sub(),mul(),div() and get the input for a & b inside every function from the user and then print the result.

def painter():
    print("Painting")


painter()

def add():
   # a=int(input("Enter a value for a:"))
    #b=int(input("Enter a value for b:"))
    print(a+b)

def sub():
    #a=int(input("Enter a value for a:"))
    #b=int(input("Enter a value for b:"))
    print(a-b)
    
def mul():
    #a=int(input("Enter a value for a:"))
    #b=int(input("Enter a value for b:"))
    print(a*b)

def div():
    #a=int(input("Enter a value for a:"))
    #b=int(input("Enter a value for b:"))
    print(a/b)
    
painter()
add()
sub()
mul()
div()

# Get an integer number from user and pass it to the function called find_even_or_odd().Let the function print whether the number is even or odd.

def find_even_or_odd(num):
    if (num%2==0):
        print("Even number")
    else:
        print("Odd number")

find_even_or_odd(int(input("Enter an integer:")))

#Get input for a and b and pass it to the function called printrange().Let the function print numbers from a to b.

def printrange(a,b):
    for i in range(a,b+1):
        print(i)

a=int(input("Enter a:"))
b=int(input("Enter b:"))
printrange(a,b)



































    

