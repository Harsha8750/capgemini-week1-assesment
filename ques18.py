weight=float(input("Enter your weight in kgs: "))
height=float(input("Enter your height in meters: "))
h=height*height
bmi=weight/h
if bmi<18.5:
    print("You are underweight")
elif bmi>18.5 and bmi<=24.9:
    print("You are normal")
elif bmi>=25 and bmi<29.9:
    print("You are overweight")
else:
    print("You are obese")

