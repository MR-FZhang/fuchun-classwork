
linkedList = [
    ["Banana", "Strawberry", "Melon", "Lemon", "Blueberry"],
    [0, 4, 3, 2, 1]
]

sortedList = []
count = 0

while count in range (0,len(linkedList[0])):
	item = linkedList[1].index(count)
	print(count)
	print(item)
	sortedList.append(linkedList[0][item])
	count = count + 1
#end while
print(sortedList)

linkedList = [
    ["Banana", "Strawberry", "Melon", "Lemon", "Blueberry"],
    [0, 4, 3, 2, 1]
]
sortedList = []
count = 0

while count in range (0,len(linkedList[0])):
	item = linkedList[1][count]
	sortedList.append(linkedList[0][item])
	count = count + 1
#end while
print(sortedList)
