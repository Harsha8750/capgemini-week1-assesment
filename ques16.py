initial_list=input("Enter numbers separated by space").split()
even_list=[]
odd_list=[]
n=len(initial_list)
for i in range(len(initial_list)):
    
    if i%2==0:
        even_list.append(i)
    else:
        odd_list.append(i)
print(odd_list)
print(even_list)
