
OutletSales = [[10, 12,15,10],[5,8,3,6],[10,12,15,10]]
total= 0
for x in range (3):
    for i in range (4):
          print ('Total for quarter',(i+1),OutletSales[x][i])
          total = OutletSales[x][i]  
    print ('Total of the OutletSales',(x+1),'is',total)
    total = 0
    print()