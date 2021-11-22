# msg = input(">")
# message = msg.split()
# print(message)
# emojis ={
# ":)" : '😄',
# ":(" : '🙁'
# }
# output=""
# for char in message:
#     output += emojis.get (char,char) + " "
# print(output)

string = input("input your string: ")
list = []
list2 = []
for char in (string):
    list.append(char)
#next char
palindrone=False
length = (len(list))
while length >0:
    list2.append(list[length-1])
    length -= 1
if list == list2:
    palindrone = True
else:
    not palindrone
    
print(list)
print(list2)

print ( palindrone)