# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 02:42:15 2023

@author: pc
"""

number = int(input("Enter the number : "))
asalMi = True

for x in range(2,number):
    if (number % x) == 0:
        asalMi = False
        break

if asalMi == True:
    print("ASAL")
else:
    print("ASAL DEGIL")