# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 17:45:34 2022

@author: My Computer
"""

class Mathematics:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
        
    def addition(self):
        return self.num1 + self.num2
    
    def substraction(self):
        return self.num1 - self.num2
    
    def division(self):
        return self.num1 / self.num2
    
    def multiplication(self,num1,num2):
        return self.num1 * self.num2
    
math = Mathematics(45,56)
print("Division = " + str(math.division()))
print("Sum = " + str(math.addition()))
