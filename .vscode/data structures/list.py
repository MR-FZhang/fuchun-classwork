#index1=0
#index2=0
#list1 = [2,5,15,36,47,56,59,78,156,244,268]
#list2 = [18,39,42,43,66,69,100]
#list3=[]
#i =len(list2)+1
#while index1<len(list1) and index2<len(list2):
#    if list1[index1]<list2[index2]:
#        list3.append(list1[index1])
#        index1=index1+1
#    else:
#        list3.append(list2[index2])
#        index2=index2+1
#
#while i in range (len(list2)+1,len(list1)):
#        item=list1[i]
#        list3.append(item)
#        i=i+1
#
#print(list3)
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



