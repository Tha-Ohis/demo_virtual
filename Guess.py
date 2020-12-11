# word="Spooky"
# name=input("Enter your name: ")
# guess=input("Enter your Guess Word: ")
# if word==guess:
#     print("You have won")

#Another Guess Game
print("\t \tHY THERE, READY TO TRY YOUR LUCK" )
score=0
num =(int(input("Guess a number: ")))
if num in range (10,15):
    print("Smart move, num is correct, move on to the next round")
    score +=1

    x = (input("Guess a word: "))
    if x == "sigh":
        print("Applaudise, You have advanced to the last level")
        score +=1

        y = (input("Guess a color: "))
        if y == "blue":
            print("Congrats, You have passed the test")
            score +=1

print(f"Total score: {score}")