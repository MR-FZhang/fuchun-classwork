def test1():
    print("hello world")
#end procedure


#main porgram starts here
test1()
name=input("what is your name?")
print("enter table, start num and end num")
table =int(input())
startnum=int(input())
endnum=int(input())

def multiple(start,end,value):
    for x in range(startnum,endnum+1):
        print(x*table)



