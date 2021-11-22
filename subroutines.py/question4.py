#subroutines
def carpark1(carpark):
    carpark= []
    for y in range (20):
        carpark.append([])
        for x in range(6):
            carpark[y].append("empty")
    print(carpark)
#end procedure

def carpark2(regnum,index,pos,carpark):
    carpark[index-1][pos-1]=regnum
    print(carpark)
    print(carpark[index-1][pos-1])
#end procedure

def carpark3(carpark,regnum):
    for row in carpark:
        for col in row:
            if col == regnum:
                col = 'empty'
            #end if
        #next col
    #next row 
#end procedure

# main program  
print("1. Reset all spaces in the car park to 'empty'")
print("2. Park a car")
print("3. Remove a car")
print("4. Display the car park grid")
print("5. Quit\n")
option = input("Enter your choice: ")
done=False
while option != "5" :
    if option == "1":
        carpark1()
    if option == "2":
        regnum = (input("what is your registration number: "))
        index = int(input("what row is your car in: "))
        pos = int(input("what column is your car in: "))
        carpark2(regnum,index,pos)
    elif option == "3":
        regnum = (input("what is your registration number: "))
        carpark3(regnum)
    elif option == "4":
        print(carpark1)
    # end if 
    option = ("Invalid choice - please re-enter: ")
    print("1. Reset all spaces in the car park to ‘empty’")
    print("2. Park a car")
    print("3. Remove a car")
    print("4. Display the car park grid")
    print("5. Quit\n")
    option = input("Enter your choice: ")
    #end while
print("Goodbye") 
#end program





