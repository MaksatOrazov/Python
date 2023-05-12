# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 03:21:00 2023

@author: pc
"""

number = int(input("Enter the number : "))
factorial = 1

if number == 0:
    print("Result is 1")
elif number < 0:
    print("The number is negative")
else:
    for i in range(1,number+1):
        factorial = factorial * i
    print("Result : ",factorial)
    