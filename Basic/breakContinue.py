# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 13:11:21 2022

@author: My Computer
"""

cities = ["Ankara", "Balikesir", "Istanbul"]

#Break
for city in cities:
    if city == "Istanbul":
        break
    print(city)
    
print("----------------------------------------------------------")
#Continue
for city in cities:
    if city == "Ankara":
        continue
    print(city)