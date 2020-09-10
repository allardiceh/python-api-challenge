myList = ["Michael", "Dinh", 26, True]
print(myList, type(myList))

myList.append('Sleeping')
print(myList)

print(myList.index("Sleeping"))

myList[4] = 'Cooking'
print(myList)

myList.remove('Cooking')

print(myList)
myList.pop(0)
myList.pop(-1)
print(myList)

myTuple = ('Python', 100, 'VBA', False)