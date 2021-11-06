
pupil_test=[[1,2,3,4,5,6,7,8,9,10],[1,4,0],[4,6,7,9]]
test=0
total=0
student=0
while len(pupil_test[test])==10:
    while (pupil_test[test]) and student in range(0,10):
        total=total+pupil_test[test][student]
        student=student+1
    print ("pupil test",test+1,"=",total/10)
    test=test+1



