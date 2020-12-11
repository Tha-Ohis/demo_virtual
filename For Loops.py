#EXAMPLE 1.....
# word = "P-y-t-h-o-n- -p-r-o"
# i = 0
# for i in word:
#     if i == "-":
#         continue
#     print(i)


#Example 2....
friends = ["a", "b", "c", "d", "e"]

for friend in friends:
    if friends.index(friend) % 2 != 0:
        continue
    print(f"Hello {friend}")
