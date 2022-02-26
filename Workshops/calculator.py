# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 15:06:50 2022

@author: My Computer
"""

def add(num1,num2):
    return num1 + num2
def substract(num1,num2):
    return num1 - num2
def multiply(num1,num2):
    return num1 * num2
def divide(num1,num2):
    return num1 / num2


print("Operation : ")
print("1 : Add")
print("2 : Substract")
print("3 : Multiply")
print("4 : Divide")

operation = int(input("Select Operation : "))
num1 = int(input("1st number : "))
num2 = int(input("2nd number : "))


if operation == 1:
    print("Addition : " + str(add(num1,num2)))
elif operation == 2:
    print("Substraction : " + str(substract(num1,num2)))
elif operation == 3:
    print("Multiplication : " + str(multiply(num1,num2)))
elif operation == 4:
    print("Division : " + str(divide(num1,num2)))
else:
    print("Wrong selection!")
    
    
