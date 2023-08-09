# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 15:26:25 2023

@author: pc
"""


from random import randint

print("Enter the number between 1 and 100")
random = randint(1,100)
print("press 0 to exit")
n = int(input("Number : "))
count = 1
while not(n == 0 or n == random):
    if n > random:
        print("Enter smaller number")
    else:
        print("Enter bigger number")
    count = count + 1
    n = int(input("Number again : "))
if n != 0:
    print("You found it in " + str(count) + " tries")
