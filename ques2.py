print("To convert celsius to farenhit enter 1")
print("To convert celsius to kelvin enter 2")
print("To convert farenhit to celsius enter 3")
print("To convert farenhit to kelvin enter 4")
print("To convert kelvin to celsius enter 5")
print("To convert kelvin to farenhit enter 6")
n=int(input("Enter your choice"))
def celtofaren(a):
    faren=((9/5)*a)+32
    print(f"The given temperature in farenhit is: {faren}")
def celtokel(b):
    kel=b+273.15
    print(f"The given temperature in kelvin is: {kel}")
def farentocel(c):
    cel=(c-32)*(5/9)
    print(f"The given temperature in celcius is: {cel}")
def farentokel(d):
    kel=((d-32)*(5/9))+273.15
    print(f"The given temperature in kelvin is: {kel}")
def keltocel(e):
    cel=e-273.15
    print(f"The given temperature in celcius is: {cel}")
def keltofaren(f):
    faren=((f-273.15)*(9/5))+32
    print(f"The given temperature in farenhit is: {faren}")
if n==1:
    a=int(input("Enter temperature in celcius: "))
    celtofaren(a)
elif n==2:
    b=int(input("Enter temperature in celcius: "))
    celtokel(b)
elif n==3:
    c=int(input("Enter temperature in farenhit: "))
    farentocel(c)
elif n==4:
    d=int(input("Enter temperature in farenhit: "))
    farentokel(d)
elif n==5:
    e=int(input("Enter temperature in kelvin: "))
    keltocel(e)
elif n==6:
    f=int(input("Enter temperature in kelvin: "))
    keltofaren(f)
