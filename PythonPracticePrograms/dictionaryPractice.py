myDict = {'Name':'Dhiraj','Surname':'Ambure', 'rollNo':1, 'DOB':16071990, 'Marks':[91,87,92,84,89]}

print(type(myDict))

print(dir(myDict))

keyList = myDict.keys()
print("List of Keys in given dictionary are {}".format(keyList))

valueList = [val for val in myDict.values()]
print(valueList)

myConvDict = dict([('a',123),('b',456)])
print(myConvDict)

""" Direct Access dictionary values using keys"""
val1 = myDict.get('rollNo')
print(val1)

print(len(myDict))
"""Add or Modify elements in Dictionary"""
#Adding an element in dictionary

myDict['Division']='A'
print(myDict)

#Updating an element in Dictionary

myDict['Name'] = 'Priyanka'
print(myDict)

print(type(myDict))

"""Delete or Remove the Element from Dictionary"""
"""
1. pop()
2. del
3. clear()
"""

"""
1. pop()
 - pop() can be used to delete any specific item from the dictionary
 - pop() method takes on arguement, i.e. key of the element to be deleted
"""

popped = myDict.pop('Division')
print("Popped Item: ",popped)

"""
2. clear()
 - clear() method clears all the elements from the dictionary
 - Empty dictionary remains
"""

myDict.clear()
print("Dictionary after using clear() method: ",myDict, "its type is: ",type(myDict))

"""
3. del
 - del operator is used to complete delete the dictionary
"""

del myDict
# print("myDict dictionary is deleted using del operator", id(myDict))

