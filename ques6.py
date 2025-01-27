def isPrime(n):
    cnt=0
    for i in range(1,n+1):
        if n%i==0:
            cnt+=1
    if cnt==2:
        return True
    else:
        return False
    
num1=int(input("Enter the starting number: "))
num2=int(input("Enter the ending number: "))
for i in range(num1,num2+1):
    if isPrime(i):
        print(i)
