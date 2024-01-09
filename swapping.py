#Write a program to swap the first and last element in the list.

list1=[1,2,3,4,5,6]
temp=list1[0]
list1[0]=list1[-1]
list1[-1]=temp
print(list1)
