# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 11:05:12 2023

@author: pc
"""

lights = ["Red","Yellow","Green"]
currentLight = lights[2]
print(currentLight)

if currentLight == "Red":
    print("STOP!")
elif currentLight == "Yellow":
    print("READY!")
else:
    print("GO!")