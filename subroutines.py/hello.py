command=""
start=False
while True:
    command=input(">").lower()
    if command=="start":
        if start:
            print ("your car has already started")
        else:
            start=True
            print("your car has started")
    elif command=="stop":
        if not start:
            print("car has already stopped")
        else:
            start=False
            print("car stopped")
    if command =="help":
        print("""
start - start the car
stop - to stop the car 
quit - the exit the program
        """)
    elif command=="quit":
        break
    else:
        print("sorry i don't understand")
#end while