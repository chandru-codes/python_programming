# String Slicing

str1="Chandrasekar"
# We need to slice only chand.
print(str1[0:5:1])
first_string=string[:half]
    second_string=string[half:]

#palindrome
str1 =input("Enter a string:")
rev_str1=str1[::-1]
if(rev_str1== str1):
    print("The entered string is palindrome")
else:
    print("The entered string is not a palindrome")

#symmetrical

string=input("Enter a string:")
half=int(len(string)/2)

if(len(string) % 2 == 0):
    first_string=string[:half]
    second_string=string[half:]

else:
    first_string=string[:half]
    second_string=string[half+1:]

if(first_string==second_string):
    print(string,"is Symmetrical")

else:
    print("String is not symmetrical")
    
#String reverse program

name=input("Enter the string:")
length=len(name)
i=0
for n in range(-1,(-length-1),-1):
    print(name[i],"\t",name[n])
    i+=1


#Character removal in string

str="python"
print(str.replace("th",""))

#Python program to print even length words in a string

n="python code to print even length words"
s=n.split(" ")
for i in s:
    if len(i)%2==0:
        print(i)

    
    


