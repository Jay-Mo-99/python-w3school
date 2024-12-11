fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)

newlist = [x for x in fruits if "a" in x]
print(newlist)

mylist= [x.upper() for x in fruits if "a" in x]
mylist2=["hello" for x in fruits]
mylist3=[x if x !="banana"else "orange"for x in fruits]
print(mylist3)