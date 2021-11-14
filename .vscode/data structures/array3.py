
school = ["AAAA", "BBBB","CCCC","DDDD"]	
medal = [4,7,1,3]
done=False
while not done:
    result = int(input("input Medals "))
    number = int(input("Enter the school number "))
    if number or result== -1:
        for i in range(0,len(school)):
            print("School number", i+1, "School name", school[i], "Number of medals", medal[i])
    #end if
    
    elif number==0:
        done=True

    			
    elif number < 1 or number> 4:
            print("Not valid school number")
    else:
        number = number - 1
        medal[number] = medal[number] + result


		
