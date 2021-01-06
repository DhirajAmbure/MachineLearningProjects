myList = []

for i in range(4):
    temp=[]
    for j in range(3):
        temp.append(j)

    myList.append(temp)

print(myList)

myList1 = []

[myList1.append([i for i in range(3)]) for j in range(4)]

print(myList1)

print(type(myList1))

myList2 = [1,2,3,4,5,6,7]
myList3 = []

for k in myList2:
    myList3.append(k**2)

print(myList3)