
num = input("enter the number")
part=0
while len(num) != 4:
    print('Error')
    num = input("enter the number")
#end while
while len(num)==4:
  num=input("enter the number")
  while num[3] == '6' or num[3] == '7':
    print('old part')
    num=input("enter the next number")
    part=part+1
#end while  
print(part)










