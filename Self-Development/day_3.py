# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 09:32:41 2023

@author: pc
"""

#%% Loop 

n = int(input("Enter number : "))

for i in range(1, n, 2):
    print(i)
    
#%%

number = int(input("Ente the number : "))
total = 0

for i in range( 1, number + 1):
    total = total + i
print(total)

#%%
colors = [1,"Red",3,"White",5,"Yellow",0,"Black",7,"Purple"]

for color in colors:
    if color in range(0,9):
        #break
        continue
    else:
        print(color)
        
#%%

number = int(input("Enter the number : "))

total = 0

for n in range(number):
    x = int(input("Enter the x : "))
    total = total + x
print(total)

#%% Faktoriel

number = int(input("Enter the number : "))

faktoriyel = 1

for i in range(1,number +1):
    faktoriyel = faktoriyel * i
print(faktoriyel)

#%%

number = int(input("Enter the number : "))
count = 0 

for i in range(number):
    if number % i == 0:
        count = count + 1
        break
if count == 0:
    print("Asal number")
else:
    print("Not Asal number")

#%%

number = int(input("Enter the number : "))

maximum = int(input("Maximum : "))
minimum = maximum

for i in range(number - 1):
    x = int(input("Number : "))
    if x > maximum:
        maximum = x
    if x < minimum:
        minimum = x
print("Maximum number = " + str(maximum) + "\nMinimum number = " + str(minimum))

#%%

number = int(input("Enter the number : "))

for i in range(1, number + 1):
    if number % i == 0:
        print(i, end = ' ')





































