my_list = list(range(100))
#print(my_list)

my_list[1:3] = ["new"]
#print(my_list)
#print(my_list[2])

# new_list = list(range(5))
# new_list.insert(1,"new one")
# print(new_list)

# fruits = ["apple","banana"]
# tropical = ["mango","papaya"]
# fruits.extend(tropical)
# print(fruits)

# thislist = ["apple", "banana", "cherry"]
# thislist.clear()
# print(thislist)


thislist = ["apple", "banana", "cherry","durian"]


[print(x*3) for x in thislist]

# for i in range(len(thislist)):
#     print(i)
# i = 0
# while i <len(thislist):
#     print(thislist[i])
#     print(i)
#     i+=1
