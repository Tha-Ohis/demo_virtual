
def highest_number(first, second, third):
    if first > second and first > third:
        print(f"{first}is the highest number")
    elif second > first and second > third:
        print(f"{second} is the highest number")
    elif third > first and third > second:
        print(f"{third} is the highest number")
    else:
        print("Two or more numbers are equal" )

highest_number(4,55,7)  

