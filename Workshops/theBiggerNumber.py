# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 11:35:16 2023

@author: pc
"""

number1 = int(input("Number 1 : "))
number2 = int(input("Number 2 : "))
number3 = int(input("Number 3 : "))

if (number1 > number2) and (number1 > number3):
    enBuyuk = number1
elif (number2 > number1) and (number2 > number3):
    enBuyuk = number2
else:
    enBuyuk = number3

print("En buyuk sayi = " + str(enBuyuk))