lst = [1,2,3,4,5]
lst_2 = ["Jane", "Kemi", "Obi", "Musa"]
print(lst[1:])
print(lst[1::2])

print(lst[ :-1])
print(lst[ ::-1])

#Changing ELEMENTS using index positions (listname[index] = new_value)
lst[4] = 23
print(lst)

lst_2[3] = "Kwame"
print(lst_2)

#Adding extra ELEMENTS in a specific position using (.insert(index, value))
lst.insert(2, 17)
print(lst)

#Removing actual ELEMENTS not index positions (list_name.remove(element))
lst.remove(17)
print(lst)

#Removing actual ELEMENTS using index positions
lst.pop(3)
print(lst)

#Using Del Keyword to delete specified elements
del lst[2]
print(lst)

#To clear an entire lists content
lst_2.clear()
print(lst_2)

#To delete the entire list
del lst_2

#FUNCTIONS IN LIST
lst_3 = [2,5,1,4,1,4]
lst.append("Jungle")   #Adds extra values to a lsit
print(lst)

lst.extend(lst_3)    #ADDS A LIST TO ANOTHER
print(lst)

lst_3 = lst.copy()    #Copies a list to another
print(lst_3)

lst_3.sort()         #Arranges a lsit in ascending order
print(lst_3)