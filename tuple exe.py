#To find the size of Tuple. The size of a Tuple means the amount of memory (in bytes) taken by a Tuple object.

#1.Using getsizeof() function:

import sys
tuple1=("a","b","c","d""e")
print("size of Tuple1 :"+ str(sys.getsizeof(tuple1))+"bytes")

#2.Using inbuilt __sizeof__() method:

tuple1=('a','b','c','d','e')
print("Size of tuple1 : " + str(tuple1.__sizeof__()) + "bytes")

#To find the maximum and minimum values in a tuple:

tup=(96,54,34,89,14,57)
max_val=max(tup)
min_val=min(tup)      
print("Maximum value :" + str(max_val) + "\nMinimum value :" + str(min_val))

#To Sum the elements of a Tuple in Python:

tup=(96,54,34,89,14,57)
print(sum(tup))

#Row-wise element Addition in Tuple Matrix

#matrix = ((1, 2, 3),
#          (4, 5, 6),
#          (7, 8, 9))

t1=(1,2,3)
t2=(4,5,6)
t3=(7,8,9)

l1=list() #To store the result

for i in range(3):
    sum=t1[i]+t2[i]+t3[i]
    l1.append(sum)

print(l1)

# To create a list of tuples from given list having number and its cube in each tuple:

numbers=[1,2,3,4,5,6]
res=[(num,num**3) for num in numbers]
print(res)

