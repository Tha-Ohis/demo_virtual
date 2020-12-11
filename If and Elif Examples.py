#If and Elif(Else) example
#Elif is also known s the chain condition

# gen=input("Enter your gender: ")
# if gen.lower()=="m" or gen.lower()=="male":
#     print("Male!!")
# elif gen.lower()=="f" or gen.lower()=="female":
#     print("Female!!")
# elif gen.lower()=="t" or gen.lower()=="transgender":
#     print("Transgender")
# else:
#     print("Gender Unknown.")


#Nestd If example (An if within another if)
height=5.8
compl="dark"
face="round"

name=input("Enter your name: ")
if name.lower()=="grace":
    print("Please answer the following questions for verification")
    zHeight=float(input("How tall are you(FT)?: "))
    if zHeight==height:
        print("Cool, two more questions to go")
        zCompl=input("What's your complexion: ")
        if zCompl==compl:
            print("\t :) Hy Grace, longtime no see.")
        zFace=input("Sorry but, What's the shape of your face: ")
    else:
        print("Sorry, wrong person.")    
else:
    print("Thanks for using our application.")