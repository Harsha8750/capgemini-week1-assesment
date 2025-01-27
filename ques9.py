# 9. String Analysis Tool
# - Write a program to analyze a string:
# - Count vowels, consonants, digits, and special characters.
# - Reverse the string and display the result.
def isVowel(c):
    if c=='A' or c=='E' or c=='I' or c=='O' or c=='U' or c=='a' or c=='e' or c=='i' or c=='o' or c=='u':
        return True
    else:
        return False
def isConsonant(c):
    if c=='B' or c=='C' or c=='D' or c=='F' or c=='G' or c=='H' or c=='J' or c=='K' or c=='L' or c=='M' or c=='N' or c=='P' or c=='Q' or c=='R' or c=='S' or c=='T' or c=='V' or c=='W' or c=='X' or c=='Y' or c=='Z' or c=='b' or c=='c' or c=='d' or c=='f' or c=='g' or c=='h' or c=='j' or c=='k' or c=='l' or c=='m' or c=='n' or c=='p' or c=='q' or c=='r' or c=='s' or c=='t' or c=='v' or c=='w' or c=='x' or c=='y' or c=='z':
        return True
    else:
        return False
vowe=0
conso=0
dig=0
special_char=0
str=input("Enter the string")
n=len(str)
for i in(0,n):
    if isVowel(str[i]):
        vowe+=1
    elif isConsonant(str[i]):
        conso+=1
    elif str[i]>=0 and str[i]<=9:
        dig+=1
    else:
        special_char+=1
reversed_string=str[::-1]
print(f"The reversed string is: {reversed_string}")
print(f"The number of vowels in the string are: {vowe}")
print(f"The number of consonants in the string are: {conso}")
print(f"The number of digits in the string are: {dig}")
print(f"The number of special characters in the string are: {special_char}")