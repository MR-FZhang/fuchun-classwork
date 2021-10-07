symptoms=input("what is your medical symptom")
temp=input("do you have a temperature")
if temp=="yes":
    s1=input("do you have sore throat")
    if s1=="yes":
        print("you may have a throat infection")
    #end if
    else:
        s2=input("do you have a cough")
        if s2=="yes":
            print("you have a chest infection")
        #end if
    #end else
#end if
else:
    print("Dont worry you are not ill, "+"Have a lovely day!")
