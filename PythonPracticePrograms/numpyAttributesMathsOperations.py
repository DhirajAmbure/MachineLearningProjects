# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 14:34:27 2020

@author: dambu
"""

import numpy as np

arrList = [[1,2,3,4],[3,4,5,6],[5,6,7,8],[7,8,9,10]]

npArr = np.array(arrList)
npArr2 = np.array(arrList)
print(npArr)

print(npArr.shape) #it displays the shape of the 2D array

print(npArr.ndim) #it displays the dimension of the array

print(npArr.size) #it displays the size of teh array (Total elements in the array)

print(len(npArr)) #it displays the length of the array (number of rows)

print(np.info(npArr))


##################### Mathematical Operations on the Array ########################
###################################################################################

print(npArr-npArr2)

print(np.subtract(npArr,npArr2))

print(npArr+npArr2)

print(np.add(npArr,npArr2))

print(npArr*npArr2)

print(np.multiply(npArr,3))

print(npArr/npArr2)

print(np.divide(npArr,npArr2))

print(np.exp(npArr))

print(np.sqrt(npArr))

print(npArr[npArr > 1])

print(npArr > 1)

print(np.array_equal(npArr,npArr2))
