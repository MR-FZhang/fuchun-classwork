list1 = [34,56,34,26,80,57,98,100,80,64,102,300,35,6,87,88]
list2= []

for index in range (0, len(list1)):
	if list1[index]>=80 and list1[index]<=100:
         list2.append(list1[index])


for i in range (0,len(list2)):
	item=list2[i]
	list1.remove(item)
    
print(list2,list1)


#for i in range(index1,len(list1)):
#        list3.append(list1[i])
#        i=i+1



