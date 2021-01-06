# Append squared element in another list

"""This is a normal way"""
myList1 = [1, 2, 3, 4, 5, 6]
myList2 = myList3 = []

for sq in myList1:
    myList2.append(sq**2)

print(myList2)

"""Solving the problem using list comprehensions"""

myList3 = [sq**2 for sq in myList1]
print(myList3)

###########################  Nested Comprehensions ############################
# To create list as given below
matrix = [[0, 1, 2],
          [0, 1, 2],
          [0, 1, 2],
          [0, 1, 2]]

#Using normal way

matrix1 = []

for i in range(4):
    temp = []
    for j in range(3):
        temp.append(j)

    matrix1.append(temp)

print(matrix1)

# Same can be done using Nested Comprehensions
###############################################################################

matrix2 = []
[matrix2.append([j for j in range(3)]) for i in range(4)]
print(matrix2)


matrix3 = []
[matrix3.append([l for l in range(4)]) for k in range(4)]

print(matrix3)