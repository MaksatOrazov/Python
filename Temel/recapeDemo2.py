# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 02:34:54 2023

@author: pc
"""

number = int(input("How many stars : "))
star = " "

for i in range(1,number+1):
    star = star + "*"
    print(star)