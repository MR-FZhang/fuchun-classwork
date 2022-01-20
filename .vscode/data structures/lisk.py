list1 = [2,5,15,36,47,56,59,78,156,244,268]
list2 = [18,39,42,43,66,69,100]
newlist = []

index = 0
index1 = 0
counter = 0
while index in range(len(list2)) or index1 in range (len(list2)):
    if list1[index] < list2[index1]:
        newlist.append(list1[index])
        index += 1
    else :
        newlist.append(list2[index1])
        index1 += 1

for x in list1:
    if newlist.count(x)==0:
        newlist.append(x)
print(newlist)