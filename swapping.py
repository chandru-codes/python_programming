#Write a program to swap the first and last element in the list.

list1=[1,2,3,4,5,6]
temp=list1[0]
list1[0]=list1[-1]
list1[-1]=temp
print(list1)

#Given a list in Python and provided the positions of the elements, write a program to swap the two elements in the list. 
#Input : List1 = [23, 65, 19, 90]
#Output : [19, 65, 23, 90]

list1=[23,65,19,90]
temp=list1[0]
list1[0]=list1[2]
list1[2]=temp
print(list1)

#Find the Length of a List Using len() Function.

list1=[23,65,19,90]
print(len(list1))

#Given two numbers, write a Python code to find the Maximum of these two numbers.

def maximum(a,b):
    if(a>=b):
        return a
    else:
        return b

a=int(input("Enter a:"))
b=int(input("Enter b:"))
print(maximum(a,b))

#Given two numbers, write a Python code to find the Minimum of these two numbers.

def minimum(a,b):
    if(a>=b):
        return b
    else:
        return a

a=int(input("Enter a:"))
b=int(input("Enter b:"))
print(minimum(a,b))
