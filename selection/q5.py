location =input("are you at home")

if location =="no":
  sensor= input("is there a movement")
  if (sensor=="yes"): 
    alarm = True
    if (alarm):
      print("an intrusion was detected")
    #end if
  #end if  
else:
  print ("alarm is off")




