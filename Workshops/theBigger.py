# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 17:07:08 2022

@author: My Computer
"""

number1 = int(input("1st number : "))
number2 = int(input("2nd number : "))
number3 = int(input("3rd number : "))

if (number1 > number2) and (number1 > number3):
    print("The bigger is  1st number : " + str(number1))
elif (number2 > number1) and (number2 > number3):
    print("The bigger is 2nd number : " + str(number2))
else:
    print("The bigger is 3rd number : " + str(number3))