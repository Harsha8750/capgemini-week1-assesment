bill_amount=int(input("Enter the total bill amount: "))
n=int(input("Enter number of people present: "))
tip=int(input("Enter the tip amount in percentage: "))
tip_amount=(tip/100)*bill_amount
individual_amount=(bill_amount+tip_amount)/n
print("Each person has to pay: ",individual_amount)