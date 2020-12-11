# #Write a program that accepts the name, hours worked a day, and displays the wage of the person
name=input("Enter your Name: ")
hrs=float(input("Enter the No of Hours Worked in a day: "))
rate=20*hrs
wage=(f"You've earned {rate}$")
print(wage)

# #Write a program that takes in the sides of a rectangle and displays its area and perimeter
name=input("Enter your name: ")
length=int(input("Enter the Length of a rectangle: "))
width=int(input("Enter the width of a rectangle: "))
area=length*width
print(f"The area of the rectangle is:{area}")
perimeter=(2*length + 2*width)
print(f"The perimeter of the rectangle is:{perimeter}")