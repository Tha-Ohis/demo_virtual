#Posting Assignment 
print("CHECK YOUR POSTING STATUS")
name=input("Enter name: ")
age=int(input("Enter age: "))
sex=input("Sex(m,f): ")
marital_status=input("Marital Status(Y,N): ")
if sex.lower()=="f" or sex.lower()== "female":
    print("You can work only in urban areas")
elif sex.lower()=="m" or sex.lower()== "male" and age in range(20, 41):
    print("You can work anywhere")
elif sex.lower()=="m" or sex.lower()== "male" and age in range(40,61):
    print("You can work only in urban areas.")
else:
    print("Error input.")
