import timeit as ti

start = ti.default_timer()

varList11 = [1,2,4,'Banana','Apple',12.5,8,9]
varList22 = [7,10,11,12]

del varList11[6]

#Copy function of List
'''This function is used to copy the list'''
copiedList33 = varList11.copy()
print("Copied List is: ",copiedList33)
print(id(varList11),"&&", id(copiedList33))

#Remove function for list
len_list = len(varList11)
varList11.remove('Banana')
print("After removing the last item from list: ", varList11)

#Append an item in the List
varList11.append('appended Item')
print("After Appending: ",varList11)

#Append list into another List
varList11.append(varList22)
print("After Appending a List into another list: ",varList11)

#Extend Method
varList11.extend(varList22)
print("After using extend method: ",varList11)
varList11.extend("Dhiraj")
print(varList11)

#Pop method
poppedEle = varList11.pop(1)
print("After using pop method: ", varList11, "Popped Element is:",poppedEle)

poppedEle = varList11.pop()
print("After using pop method: ",varList11, "Popped Element is:",poppedEle)

#Use count method on list
print("Count method on List: ",varList11.count(2))

#Index method on List
print("Index of 12.5 is: ",varList11.index(12.5))
#print("Index of 30 is: ",varList11.index(30))

#Insert method
varList11.insert(4,11.5)
print("List after inserting 11.5 at position 4: ", varList11)

#Reverse method
varList11.reverse()
print("Reversed List: ", varList11)

#Sort Method
varList22.sort(reverse = False)
print('Sorted List: ',varList22)


'''To use sort methods, list should contain values of same data type'''

print(max(varList22))

print(sum(varList22))

valSet = ()
print(type(valSet))

varList22.clear()
print("Cleared List",varList22)


varList33 = [2,8,4,3,7,9,5]
popp = varList33.pop()
print(popp)

rangeList = [i for i in range(20)]
print(rangeList)

end = ti.default_timer()

print("Time taken to execute the Python Code is: ",(end-start))