num=int(input("Enter any number: "))
def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f
if num<0:
    print("You have entered a negative number")
    print("Factorial is applicable for only positive numbers")
    print("Please enter a positive number")
    
else:
    print(fact(num))
