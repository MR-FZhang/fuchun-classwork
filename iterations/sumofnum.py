import time


# List = [3,6,2,8,1]
# total = 0
# for i in (List):
#   total = total + i 
# print (total)
# pos = 0
# while pos in range(0,len(List)-1):
#   total = total + List[pos]
#   pos += 1
# print (total)

# def addnums (numbers):
#   sum= 0
#   for n in numbers:
#     sum = sum +n

#     return sum
# def rADDNUMBS (numbers):
#   index = 0
#   if len(numbers) == 1: 
#     return numbers[index]
#   else:
#     return numbers[index] + rADDNUMBS(number.remove(index[0]))
# #end function
# number = [3,6,2,8,1]
# rADDNUMBS(number)

# def addnums(numbers):
#   if numbers <= 0:
#     return 0
#   if numbers%2 == 0:
#     numbers += addnums(numbers-2)
#     return numbers
#   else:
#     return 0 
# #end function
# numbers =  10
# print (addnums(numbers))
# start_time = time.time()
# for i in range(2,5):
  # print (i)  
# endTime1 = time.time()
# total_time = endTime1 - start_time
# print (total_time)

def fib(n):
	if n <= 1000:
		if n <= 1:
			return n
		else:
			return fib(n-1) + fib(n-2)
		#end if
	else: 
		return 0
  #endif
#endfunction

def fibonacci2(n):
  fibNumbers = [0,1,1] 
  if n <= 30 and n >= 3:  
    for i in range (3, n+1):
      fibNumbers.append(fibNumbers[i-1] + fibNumbers[i-2])
    #next i
    return fibNumbers[n]
  else : 
    return 0
#endfunction

start_time1 = time.time()
print (fib(0))
endTime1 = time.time()
total_time1 = endTime1 - start_time1
print (total_time1)

start_time2 = time.time()
print(fibonacci2(40))
endTime2= time.time()
total_time2 = endTime2 - start_time2
print (total_time2)
