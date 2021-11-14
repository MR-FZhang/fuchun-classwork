
linkedList = [
    ["Banana", "Strawberry", "Melon", "Lemon", "Blueberry"],
    [0, 4, 3, 2, 1]
]
sortedList = []
count = 0

while count in range (0,len(linkedList[0])):
	item = linkedList[1].index(count)
	sortedList.append(linkedList[0][item])
	count = count + 1
#end while
print(sortedList)

for i in range(index1,len(list1)):
    list3.append(list1[i])
    i=i+1




# Data=[ ["Banana",4], ["Strawberry"], ["Melon",1], ["Lemon",2], ["Blueberry",3]]
# Linked_list=[]
# Count=0
# Pointer=0
# while Count<len(Data):
#     while Pointer in range(0,len(Data[Count])):
#         Linked_list.append(Data[Count][Pointer])
#         Pointer=Pointer+1
#         Count=Data[Count][Pointer]
#         Pointer=0
#     #End While
#     Count=Count
# #End While

# Data=[ ["Banana","4"], ["Strawberry"], ["Melon",1], ["Lemon",2], ["Blueberry",3]]
# data = [
#     ['banana', 'apple'],
#     [4, 1]
# ]
# Count=str(0)
# Pointer=1
# Count=Data[0][1]
# print(Count)

# data[1].pointer
