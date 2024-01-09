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
