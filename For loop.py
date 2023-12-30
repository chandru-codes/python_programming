# 1)Get input for number a and b. print the number between a & b.

a=int(input("Enter a number:"))
b=int(input("Enter another number:"))
for i in range(a+1,b):
 print(i)

# 2)Print even number between 1 to 10.

for i in range (1,11):
 if(i%2==0):
     print(i)

'''3)Expected output:
    week 1:
         Day : 1
         Day : 2
         Day : 3
     week 2:
         Day : 1
         Day : 2
         Day : 3

SOLUTION: '''
for i in range(1,3):
    print("Week:",i)
    for j in range(1,4):
          print("Day:",j)

'''4)Expected output:
    1
    1 2
    1 2 3
    1 2 3 4

SOLUTION:'''

for i in range (1,5):
 print()
 for j in range(1,i+1):
     print(j,end="")
  

    
