def getpword(attempt):
    global Done
    Done=False
    while not Done:
        if attempt==1:
            password1 = input("enter the password: ")
            password2 = input("re-enter the password: ")
        #end if 

        while password1 != password2:
            print("error, password do not match")
            password1 = input("enter the password: ")
            password2 = input("re-enter the password: ")        

        while password1==password2 and not Done:
            if len(password2) <6 or len(password2)>8 :
                 password1 = input("enter the password: ")
                 password2 = input("re-enter the password: ")
            if  len(password2) >=6 and len(password2)<=8 :
                print("you have successfully changed the password: ")
                Done=True
        Done=True
            # end if   
        #end while
    #end while

Done=False
getpword(1)	
		
# pass multiple results back from a function
#def calc(a,b):
#    constantVal = 2
#    x = constantVal *(a + b)
#    y = a - b
#    z = a * b
#    return x, y, z
#
##main program
#add, subtract, multiply = calc(5,3)
#print (add, subtract, multiply)


