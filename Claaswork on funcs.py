#Number 1

# def count_letter(word, letter):
#     count = 0
#     for alpha in word:
#         if alpha == letter:
#             count += 1
#     return count

# count = count_letter("banana", "a")
# print(count)

#Number 2
# def slicer(word):
#     print(word[0:2])

# slicer("better")

#Number 3
# def started(word, letter):
#     if word[0] == letter:
#         return True
#     else:
#         return False 
# start= started("Rather", "R")
# print(start)


#Number 4







#Number 5
# num=int(input("Enter a number: "))
# if num % 3==0 and num % 5==0:
#     print ("FizzBuzz")
# elif num % 3==0:
#     print ("Fizz")
# elif num % 5==0:
#     print ("Buzz")
# else:
#     print(f"{num}, is not a multiple of 3 or 5")





#Number 6
while True:
    word=input("Enter a word: ")
    if word=="quit":
        break
    else:
        print(word)