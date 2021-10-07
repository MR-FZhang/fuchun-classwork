exam= int(input("enter exam score"))
a = int(input("enter attendance"))
if (exam>90 and a>90):
    print("A")
elif((exam>80 and exam<=90)and (a>90)):
    print("B")
elif((exam>70 and exam<=80)and (a>90)):
    print('C')
elif((exam<=70)and (a>90)):
    print("FAIL")
elif((exam>90)and (a<=90)):
    print("FAIL")
elif((exam>80 and exam<=90)and(a<=90)):
    print("FAIL")
elif((exam>70 and exam<=80)and(a<=90)):
    print("FAIL")
elif((exam<=70)and (a<=90)):
    print("FAIL")
#end if

