n=int(input("Enter any number to generate table: "))
rang=int(input("Please specify the range of the table: "))
for i in range(1,rang+1):
    print(n,"* ",i," = ",n*i)