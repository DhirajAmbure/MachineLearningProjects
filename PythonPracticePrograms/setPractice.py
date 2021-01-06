"""
Set
"""

###### Adding item in Set ###########

mySet = {1,4,2,'add'}
mySet.add('sub')

myset2 = {'abc':7,'pqr':8,'xyz':9,'mul':5}
mySet.update(myset2)

print(mySet)

# Using update method to add multiple values

mySet.update(j for j in range(6,10))
print(mySet)

myEmptySet = set()
myEmptySet.update(i for i in range(9,20))
print(myEmptySet)
print("minimum value from set is: ", min(myEmptySet))

######## Removing Item from Set ################
""" Methods Used
# 1. remove()
# 2. discard()
# 3. pop()
# 4. clear()
"""

""" 1. remove()
 - An item to be removed is passed as a parameter
 - If item is not present in the set, then it throws ValueError
"""

myEmptySet.remove(11)
print(myEmptySet)

#myEmptySet.remove(11)
#print(myEmptySet)

""" 2. discard()
 - An item to be discarded is passed as a parameter
 - If item is not present in the set, then it doesn't throw ValueError
"""

myEmptySet.discard(12)
print(myEmptySet)

myEmptySet.discard(12)
print(myEmptySet)

""" 3. pop()
 - No argument is passed as a parameter
 - A random item is popped from the set and it is returned
 """

poppedItem = myEmptySet.pop();
print("Popped item is {}".format(poppedItem))

""" 4. clear()
 - It will clear the entire set
 - An empty set remains
 """

myEmptySet.clear()
print("Set after using clear function is ",myEmptySet)

myEmptySet.update(k for k in range (1,12))
print(myEmptySet)

""" 5. del
 - It will delete the entire set
 - Reference of the set is also deleted, means that set can't be accessed using the same variable name
 """
del myEmptySet
# print(myEmptySet)

"""
Python Set Operations
 - Union
 - Intersection
 - Symmetric Difference
 - Subset
"""

mySet1 = {1,2,3,4,5}
mySet2 = {3,6,7,5,8}


"""
- Union of 2 sets using | operator
- union() method can also be used
"""

print("Union of both sets using | operator is: ", mySet1 | mySet2)

myUnionSet = mySet1 | mySet2

print(myUnionSet)

myUnionSet2 = mySet1.union(mySet2)

print("Union using method is: ", myUnionSet2)


"""
- Intersection of 2 sets using & operator
- intersection() method can also be used
"""

myInterSet1 = mySet1 & mySet2
print("Intersection of both sets using & operator is: ",myInterSet1)

myInterSet2 = mySet1.intersection(mySet2)
print("Intersection of both sets using intersection() method is: ", myInterSet2)

"""
- Difference is elements present in set 1 but not in set 2
- Difference can be found using - operator or difference() method
"""

myDiffSet1 = mySet1 - mySet2
print("Difference between mySet1 and mySet2 using - operator is: ", myDiffSet1)

myDiffSet2 = mySet2.difference(mySet1)
print("Difference between mySet2 and mySet1 using difference() method is: ", myDiffSet2)
print(myDiffSet2)

sortedList = sorted(myDiffSet2)
print(sortedList)

"""
- Symmetric Difference is gives set of elements from both sets except those that are common in both sets
- Symmetric difference can be found using ^ operator or symmetric_difference() function
"""

mySymmDiffSet1 = mySet1^mySet2
print("Symmetric Difference using ^ operator is: ",mySymmDiffSet1)

mySymmDiffSet2 = mySet1.symmetric_difference(mySet2)
print("Symmetric Difference using symmetric_difference() method is: ",mySymmDiffSet2)

"""
- subset, Set 1 can be subset of Set 2 only if all its elements are present in Set 2
- if a set is subset or not can be found using issubset() method, which returns a boolean value
"""

mysetOne = {3,4,5}
mysetTwo = {5,6,3,5,2,4}

print("Is set mysetOne a subset of mysetTwo",mysetOne.issubset(mysetTwo))
print("Is set mysetTwo a subset of mysetOne", mysetTwo.issubset(mysetOne))

"""
- Superset, Set 1 can be superset of set 2 if all set 2 items are present in set 1
- if a set is Superset or not can be found using issuperset() method. which returns a boolean value
"""

print("Is mysetTwo a superset of mysetOne", mysetTwo.issuperset(mysetOne))
print("Is mysetOne a superset of mysetTwo", mysetOne.issuperset(mysetTwo))

"""
- Isdijoint() method is used to find if two sets are disjoint (Meaning they do not have any item in common)
"""
myDisSet1 = {1,2,3,4}
myDisSet2 = {5,9,8,6}

print("is myDisSet1 and myDisSet2 disjoint sets?", myDisSet1.isdisjoint(myDisSet2))

"""
Frozen Sets
 - Frozen sets can be created using frozenset() method
 - Frozen sets are immutable like tuples hence we can not use add(), update() or remove(), discard() methods on Frozen Sets
 - Frozen sets support methoda like, union, issubset(), issuperset(), symmetric_difference(), intersection(), copy(), difference(), isdijoint()
"""

fset = frozenset(j for j in range(10))
print(fset)

print(len(fset))