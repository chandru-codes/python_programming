#Compile time error
try:
  print("Hi")
  print("Bye")
  printt("Hey")
except NameError as e: #printt
    print("NameError",e)

#Logical error
#To print a+b

  a=10
  b=20
  print(a+a) #a+b
#Error is not generated in this program

#Runtime Error
try:
  a=int(input())#10
  b=int(input())#ten
  print(a+b)
except ValueError as e:
    print("ValueError",e)

#Type error
try:
  a=int(input())
  b=input() #string
  print(a/b) # string cannot be used in division.

except TypeError as e:
    print("TypeError",e)

# Exception:
#valueError
try:
  a=int(input())#10
  b=int(input())#ten
  print(a+b)
except TypeError as e:
    print("TypeError",e)
except Exception:
    print("Enter in Numbers")


# Finally keyword

try:
    a=int(input())
    b=int(input())
except ValueError as e:
    print("ValueError",e)

except Exception:
    print("Something wrong")

finally:
    print(a+b)
    print("Done")













    

