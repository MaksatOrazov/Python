# -*- coding: utf-8 -*-
"""
Created on Fri May  5 10:23:13 2023

@author: pc
"""

class Person:
    def  __init__(self,firstName,lastName,age):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        
person1 = Person("Maxi","Orazov", 26)
print(person1.firstName)

class Worker(Person):
    def __init__(self,salary):
        self.salary = salary
        
        
class Customer(Person):
    def __init__(self,creditCardNumber):
        self.creditCardNumber = creditCardNumber
        
maxi = Worker()
dotde = Customer()        