# EXAMPLE 1....
# a=1
# i=10
# while a<=i:
#     print(a)
#     a+=1


#EXAMPLE 2....
# ind=0
# word= "Python Programming"
# length= len(word)
# while ind < length:
#     print (word[ind], end = ",")
#     ind+=1


#EXAMPLE 3....
# user_name = input("Enter your name: ")
# num_test = int(input("How many test have you taken? "))

# if num_test <=2:
#     print("Too Small")
# else:
#     sum =0
#     count =1

#     while count <= num_test:
#         score= int(input("Enter your scores: "))
#         sum +=score
#         count += 1

#     avg = sum/count
#     print(f"{avg} is the average")


#EXAMPLE 4....INFINITE LOOP
# while True:
#     text = input("> ")
#     if text == "quit":
#         break
#     elif text == "tired":
#         continue
#     else:
#         print(text)
# else:
#     print("The Loop is done !!!")


#EXAMPLE 5.....
# sum =0
# count = 1
# print("ENTER 0 TO STOP SCORE INPUTS")

# while True:
#     score= int(input("Enter your scores: "))
#     if score==0:
#         break
#     else:
#         print(score)

#     sum +=score
#     count+=1
    
# avg = sum/count
# print(f"{avg} is the average")


#EXAMPLE 6........
# word = "P-y-t-h-o-n- -p-r-o"
# i = 0
# c = len(word)
# while i < c:
#     i += 1
#     if word[i] == "-":
#        continue        
#     else:
#       print(i)





#EXAMPLE 7......
n=2
while n<=10:
    if n % 2==0:
        print (n)
        n=n+1        
