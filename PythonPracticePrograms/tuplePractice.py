"""
Tuples are Immutable
"""

myTuple = ()
print(type(myTuple))

myTuple = (1,5,2,['Dhiraj','Priyanka'],7,6)
print(type(myTuple))
print(myTuple)

print(myTuple[2])

print(myTuple[3][0])

"""Even though Tuples are Immutable, we can change data of Mutable Datatype inside tuple"""

myTuple[3][1] = "Test"
print(myTuple)

print(myTuple[-2:])

print(myTuple[-1::-1])

print(myTuple[::-1])

'''Concatenating the Tuple'''

myTuple1 = ('One','Two','Three')
myTuple2 = myTuple+myTuple1
print(myTuple2)

print(myTuple2.count('One'))

print(myTuple2.count('Dhiraj'))     # Count of 'Dhiraj' shows ZERO as it is in List inside the Tuple

print(len(myTuple2))

print(myTuple2.index('One'))
#print(myTuple2.index(30))

# print(myTuple2.index('Four'))

'''Membership in the Tuple'''

print(8 in myTuple2)

'''Common built in functions on Tuple'''
myTuple3 = (6,2,4,1,9,7,5)
mySortedTuple = sorted(myTuple3,reverse=False)
print(mySortedTuple)

print("Lagest Number in the tuple is {}".format(max(myTuple3)))

print("Smallest Number in the tuple is {}".format(min(myTuple3)))

print("Sum of items in the Tuple is {}".format(sum(myTuple3)))

#print("Minimum value from tuple is: ",min(myTuple2))

del myTuple2
#print(myTuple2)