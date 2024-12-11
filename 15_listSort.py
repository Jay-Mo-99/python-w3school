#thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort() #Ascending order
# thislist.sort(reverse=True) #Descending order

def my_func(n):
    return abs(n-50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = my_func)
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)