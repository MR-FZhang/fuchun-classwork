test=[1,2,3]
student=0
total=0
while len(test)==3 and student in range(0,3):
    total=total+test[student]
    student=student+1
print("the average for the test is", total/len(test))
