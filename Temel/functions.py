# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 02:50:57 2023

@author: pc
"""
#%%

def sayHi(name = "Dear", surName = "User"):
    print("Hello " + name + " " + surName)
    
sayHi("Maxi","Orazov")
sayHi()

#%%

#%%

def calculateTriangle(a,b):
    return a*b/2
area = calculateTriangle(6,7)
print(area)

#%%

calculateTriangle2 = lambda a,b : a*b/2
print(calculateTriangle2(3,6))
















