total=0
oldpart=0
num='-1'
while num!='9999':
    num = input("enter the number")
    while len(num)!=4:
        num = input("Error: enter the number")
    if num=="9999":
        total=total+0
    #end if
    else:
        total=total+1
    #end else
    #end while
    
    if num[3] == '6' or num[3] == '7':
       print('old part')
       oldpart=oldpart+1
    #end if
#end while


print("old parts=", oldpart," total parts=",total)