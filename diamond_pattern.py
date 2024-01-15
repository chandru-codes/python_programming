#Half Diamond Pattern

a=1
b=5

for i in range(1,10):#[1,2,3,4,5,6,7,8,9]
    if(i<5):
        print("*"*a)
        a+=1
    else:
        print("*"*a)
        a-=1
        
#Full Diamond Pattern

a=1
b=5

for i in range(1,10):#[1,2,3,4,5,6,7,8,9]
    if(i<5):
        print((' '*b)+("*"*a)*2)
        a+=1
        b-=1
    else:
        print((' '*b)+("*"*a)*2)
        a-=1
        b+=1
