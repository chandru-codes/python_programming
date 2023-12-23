score=int(input("Enter the Score out of 100 : "))
if(score<=35):
    print("Poor Student")
elif(score>35 and score<=70):
     print("Average Student")
elif(score>70 and score<=100):
     print("Good Student")
else:
    print("Invalid Input")
