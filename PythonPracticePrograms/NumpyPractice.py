# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 12:27:19 2020

@author: dambu
"""

import numpy as np


arrList = np.array(np.arange(0,12,2))
print(arrList)

arrMulList = arrList*2

print(arrMulList)

arrZeroes = np.zeros((4,4), dtype=int)
print(arrZeroes)

arrOnes = np.ones((4,4), dtype=int)
print(arrOnes)

arrLinSpace = np.linspace(0,16,5)
print(arrLinSpace)

arrFull = np.full((2,3),7)
print(arrFull)

arrEye = np.eye(3)
print(arrEye)

arrRand = np.random.random((2,2))
print(arrRand)