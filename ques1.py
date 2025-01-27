def check_balance():
    print(f"The total amount in the bank account is: {fin_amount}")
def deposit(fin_amount,amount):
    fin_amount+=amount
    print(f"The final amount after depositing in thebank account is {fin_amount}")
def withdraw(fin_amount,amount):
    if amount>fin_amount:
        print("Insufficient balance for withdrawl")
    else:
        fin_amount-=amount
        print(f"Your total amount after withdrawl is {fin_amount}")
fin_amount=10000
amount=0
print("If you want to check balance enter 1")
print("If you want to withdraw money enter 2")
print("If you want to check balance enter 3")
n=int(input("Enter your choice: "))
if n==1:
    check_balance()
elif n==2:
    amount=int(input("Enter amount: "))
    deposit(fin_amount,amount)
elif n==3:
    amount=int(input("Enter amount: "))
    withdraw(fin_amount,amount)
else:
    print("Enter a valid option")

