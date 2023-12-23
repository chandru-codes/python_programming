#if salary is greater than or equal to 20000 or age less than or equal to 25,get input for required loan amount. If not print you are not eligible for loan.

salary=int(input("Enter your Salary : "))
age=int(input("Enter your age : "))
if(salary>=20000 or age<=25):
    
    req_loan_amt=int(input("Enter how much amount you want :"))
    if(req_loan_amt>50000):
       print("The maximum loan amount is 50000")

    else:
       print("you are eligible for loan")

else:
    print("you are not eligible for loan")
