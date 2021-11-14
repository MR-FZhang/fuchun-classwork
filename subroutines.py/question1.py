def multiple(table, startnum,endnum):
    print("Hi", name , "here is yout times table")
    for x in range(startnum,endnum+1):
        print(x*table)
    

#main porgram starts here

name=input("what is your name?: ")
print("enter table, start num and end num: ")
table =int(input())
startnum=int(input())
endnum=int(input())

multiple(table,startnum,endnum)
