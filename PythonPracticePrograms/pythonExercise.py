################### List of squared Values ###########################

normalList = [2,4,7,9,8,6]

squaredList = [i**2 for i in normalList]

print(squaredList)

#################### Make Combination of (x,x) values #################

myComboList = []

[myComboList.append()]


##################### Store only the even numbers from list #####################

mylistAll = [1,2,4,5,6,8,10,11,12,13,14,20,22,23]
listOfEvenNum = []

for i in mylistAll:
    if i%2==0 and i!=2:
        listOfEvenNum.append(i)

print(listOfEvenNum)

#using list comprehensions

listofEvenNum1 = []

[listofEvenNum1.append(j) for j in mylistAll if j%2==0 and j!=2]

print(listofEvenNum1)