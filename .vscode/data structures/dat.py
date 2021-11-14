list1 = [34,56,34,26,80,57,98,100,80,64,102,300,35,6,87,88]
delete = []
count=0
hello=0
total=0
for index in range (0, (len(list1))):
	 if (list1[index] >=80) and (list1[index] <=100):
		 count+=1
print ("Number of integers in range 80-100",count)
for index in range (0,len(list1)):

  	if (list1[index] >=80) and (list1[index] <=100):
          delete.append(list1[index])
print(delete)
for x in delete:
	item=list1.index(x)
	list1.remove(x)
print(list1)
print(f"numbers in the remaining list is {len(list1)}")
while hello in range(0,len(list1)):
	total=list1[hello]+total
	hello=hello+1
print(f"numbers in the remaining list is {total}")
print("numbers in the remaining list is", total)
print(hello)

	#end if
# print ("Number of integers in range 80-100", count)
# print(list1)

# for x in delete:
#     item = list1.index(x)
#     del list1[item]
# print(list1)
# print(item)



