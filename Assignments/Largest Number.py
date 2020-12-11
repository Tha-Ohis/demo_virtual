Largest of two Numbers Assignment
num_1=int(input("Enter a first number: "))
num_2=int(input("Enter a second number: "))
if num_1>num_2:
    print(f"{num_1} is the greater number between both numbers")
elif num_2>num_1:
        print(f"{num_2} is the greater number between both numbers")
else:
    print("Both numbers are equal")


#Largest of three numbers
num_1=int(input("Enter a first number: "))
num_2=int(input("Enter a second number:  "))
num_3=int(input("Enter a third number:"))
print(f"{max(num_1,num_2,num_3)}, is the largest number")