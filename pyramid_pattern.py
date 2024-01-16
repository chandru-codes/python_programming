
# With Spacing

r=int(input("Enter the no of rows:"))

for i in range(r): #rows
    for j in  range(r-i-1): #For column space
          print(" ",end="")
    for j in range(i+1):  #For column star
         print("*",end=" ")

    print()

# Without Spacing

r=int(input("Enter the no of rows:"))

for i in range(r): #rows
    for j in  range(r-i-1): #For column space
          print(" ",end="")
    for j in range(2*i+1):  #For column star
         print("*",end="")

    print()

