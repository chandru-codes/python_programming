# Set username="EMC" and password="123".
# Get input for username and password.
# create a function called validate.
# If username and password matches should return true else false.

username="EMC"
password="123"

a=input("username:")
b=input("password:")

def validate():
 if(username==a and password==b):
     return True
 else:
     return False

print(validate())

#Get input for a and b and function called add() which should return the sum of a and b and multiply that sum with c.
#(a+b)*c

def add(sum):
    sum=a+b
    return sum

a=int(input("Enter a:"))
b=int(input("Enter b:"))
c=int(input("Enter c:"))

ans=add(sum)*c
print(ans)


   
