salary=int(input("Enter the salary: "))
age=int(input("Enter the age: "))
credit_score=int(input("Enter the credit score: "))
if salary>=25000 and age>=18 and credit_score>=800:
    print("Your loan has been approved")
elif salary<25000 and age>=18 and credit_score>=800:
    print("Your loan is rejected as your salary is less than 25000")
elif salary>=25000 and age<18 and credit_score>=800:
    print("Your loan is rejected as your age is less than 18")
elif salary>=25000 and age>=18 and credit_score<800:
    print("Your loan is rejected as your credit score is less than 800")
else:
    print("Your loan has been rejected")
