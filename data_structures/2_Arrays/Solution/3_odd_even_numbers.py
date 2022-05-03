max = int(input("Enter max number: "))

odd_numbers = []

for i in range(1, max):
    if i % 2 == 1:
        odd_numbers.append(i)

print("Odd numbers: ", odd_numbers)




another way

num=int(input("enter a number"))
list2=[]
for i in range(1,num+1,2):
    list2.append(i)
list2
    
