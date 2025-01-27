year=int(input("Enter the year: "))
cnt=0
if year%4==0:
    if year%100==0:
        if year%400==0:
            print(f"The given year is a leap year: ")
        else:
            print("The given year is not leap year")
    else:
        print(f"The given year is a leap year: ")
else:
    print("The given year is not leap year")