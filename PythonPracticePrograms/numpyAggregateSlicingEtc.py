# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 21:34:12 2020

@author: dambu
"""
import time as t
import numpy as np

startTime = t.time()

arrList = [[1,2,3,4],[3,4,5,6],[5,6,7,8],[7,8,9,10]]

npArr = np.array(arrList)
npArr2 = np.array(arrList)

print(np.array(np.arange(0,20,2)))

print(list(range(0,20,2)))

print(np.linspace(0,18,10))

"""
Aggregate Functions of Numpy

"""

print(npArr.sum())

print(npArr.min())

print(npArr)

print(npArr.max())

print(npArr.max(axis=1))

print(npArr.max(axis=0))

print(npArr2.min())

print(npArr2.min(axis=0))

print(npArr2.min(axis=1))

print(npArr2.mean(axis=0))

print(npArr.mean(axis=1))

print(np.median(npArr2,axis=0))

print(np.median(npArr2,axis=1))

print(npArr.argmax(axis=0))

print(npArr.argmax(axis=1))

print(npArr.argmin(axis=0))

print(npArr.argmin(axis=1))

print(npArr.argmax())

print(npArr.argmin())

print(np.argmax(npArr,axis=0))

"""
Standard Deviation

"""
print(npArr.std())

print(npArr.std(axis=0))

print(npArr.std(axis=1))

"""
Sort the array

"""

npArr.sort()

print(npArr)

print(npArr[1:3])

print(npArr[::-1])

print(npArr[0:2,1:4])

print(npArr[0:3,1:4])

print(npArr[:,1:4])

i = np.transpose(npArr2)
print(i)
print(npArr2)

j = npArr2.reshape(8,2)
print(j)
print(npArr2)

print(np.concatenate((npArr,npArr2),axis=1))

print("Time Taken for execution in seconds:",(t.time() - startTime)/100)