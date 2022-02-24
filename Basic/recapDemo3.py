# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 13:23:07 2022

@author: My Computer
"""

number = int(input("Enter the number : "))
isPrime = True
for x in range(2,number):
    if (number % x) == 0:
        isPrime = False
        break
    
if  isPrime == True:
    print("Prime")
else:
    print("Not Prime")