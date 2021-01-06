varA = [10,20,10,20,30,40,50,60,50,40]
dupCnt = 0
unqList = []
dupList = []

for listMem in varA:
    if listMem not in unqList:
        unqList.append(listMem)
    else:
        dupCnt += 1
        dupList.append(listMem)

print("Data Type is: "+str(type(varA)))
print("Unique List is: ",unqList)
print("Number of duplicate values found: ",dupCnt)
print("Duplicate List is: ",dupList)