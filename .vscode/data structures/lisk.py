list1 = [2,5,15,36,47,56,59,78,156,244,268]
list2 = [18,39,42,43,66,69,100]
newlist = []

index = 0
index1 = 0
while index in range (len(list2)):
    if list1[index] < list2[index]:
        newlist.append(list1[index])
    else :
        newlist.append(list2[index1])
    index += 1

print(newlist)