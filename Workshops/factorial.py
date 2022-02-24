# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 17:17:34 2022

@author: My Computer
"""

number = int(input("Enter the number : "))

factorial = 1 


if number < 0:
    print("Negative number can not calculate the factorial!")
elif number == 0:
    print("The result is : 1 ")
else:
    for i in range(1,number+1):
        factorial = factorial * i
    print("The result is : " ,factorial)
    