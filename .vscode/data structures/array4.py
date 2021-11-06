pupils=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
group2=[]
group1=[]
index=0
while len(pupils)==20 and index<20:
   if (pupils[index]%2)== 1:
      group1.append(pupils[index])
      
   #end if
   else:
      group2.append(pupils[index])
      
   #end else
   index=index+1
print("group1",group1)
print("group2",group2)
   
  
   

