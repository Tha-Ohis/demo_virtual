def avg_score():
    score_1=int(input("Enter your first score: "))
    score_2=int(input("Enter your second sccore: "))
    total=score_1+score_2
    average= total/2
    print(average)

def check_status():
    if average >= 30:
        print("Your Average isn't high enough, sorry you have to redo the exam.")
    else:
        print("You're good to go, congratulations you don't have to redo the exam.")

        


avg_score()
check_status()
