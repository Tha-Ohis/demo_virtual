#24hrs Time construct
print("\tPY DIGITAL CLOCK")
name=(input("Enter your name: "))
time=(float(input("Enter the time in 24hr Format: ")))
if time >= 0 and time <= 12:
    print(f"Good Morning {name.upper()}")
elif time>= 13 and time <=16:
    print(f"Good Afternoon {name.upper()}")
elif time>= 17 and time <= 20:
    print(f"Good Evening {name.upper()}")
elif time>= 21 and time<= 24:
    print(f"Good Night {name.upper()}")