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
    
    


