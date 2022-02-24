# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 15:13:32 2022

@author: My Computer
"""

setA = {1,4,66,3,2}
setB = {1,2,6,3,78}

#union
print(setA | setB)
print(setA.union(setB))
print(setB.union(setA))
print("--------------------------------------------------------------------")

#intersection
print(setA & setB)
print(setA.intersection(setB))
print(setB.intersection(setA))
print("--------------------------------------------------------------------")

#difference
print(setA - setB)
print(setA.difference(setB))
print(setB.difference(setA))
print("--------------------------------------------------------------------")

#
print(setA ^ setB)
print(setA.symmetric_difference(setB))
print(setB.symmetric_difference(setA))
print("--------------------------------------------------------------------")












































