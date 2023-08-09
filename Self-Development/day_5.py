# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 21:43:05 2023

@author: pc
"""
# Work with lists

#%%
lists = []
number = int(input("Enter the number : "))
for i in range(number):
    n = int(input("Numbers : "))
    lists.append(n)
for i in range(number):
    print(lists[i], end= " ")

#%%
a = [1,23,4]
b = [3,2,4,5]
c = a + b 
print(a * 3)
print(c)


























































