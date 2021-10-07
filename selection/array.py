name=["dave","lazar","darius","tony"]
max=len(name)
myname=input("type name to find")
found=False
counter=0
while counter<max and found==False:
    if myname==name[counter]:
        print (counter+1)
        found= True
    #end if

    counter=counter+1
#end while

if found==False:
    print("name was not found")
#end if



