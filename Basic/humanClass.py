# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 18:06:56 2022

@author: My Computer
"""

class Person:
    def __init__(self,firsName,lastName,age):
        self.firsName = firsName
        self.lastName = lastName
        self.age = age
        
person1 = Person("Maksat", "Orazov", 25)
        
print(person1.firsName)
print(person1.lastName)
print(person1.age)

class Worker(Person):
    def __init__(self,salary):
        self.salary = salary
        
class Customer(Person):
    def __init__(self,creditCardNumber):
        self.creditCardNumber = creditCardNumber
        
nasir = Worker()
nasir.salary

duygu = Customer()
duygu.creditCardNumber




















