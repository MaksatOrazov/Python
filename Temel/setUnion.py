# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 08:06:03 2023

@author: pc
"""

setA = {1,2,3,4,5}
setB = {1,3,4,6,7,8}

#union
print(setA | setB)
print(setA.union(setB))

#intersection
print(setA & setB)
print(setA.intersection(setB))

#difference
print(setA - setB)
print(setA.difference(setB))
print(setB.difference(setA))

#symmetric Difference
print(setA ^ setB)
print(setA.symmetric_difference(setB))

