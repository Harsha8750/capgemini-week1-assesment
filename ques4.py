name=input("Enter the student name")
num1=int(input("Enter marks in Telugu: "))
num2=int(input("Enter marks in Hindi: "))
num3=int(input("Enter marks in English: "))
num4=int(input("Enter marks in Science: "))
num5=int(input("Enter marks in Social: "))
total_marks=num1+num2+num3+num4+num5
per=(total_marks/500)*100
print(f"Total marks: {total_marks}")
print(f"Percentage is: {per}")
if per>=80:
    print("Grade: A")
elif per<=80 and per>=65:
    print("Grade: B")
elif per<65 and per>=55:
    print("Grade: C")
elif per>55 and per>=35:
    print("Grade :D")
else:
    print("Fail")