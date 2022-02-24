# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 13:19:28 2022

@author: My Computer
"""

number = int(input("How many stars : "))

star = ""

for x in range(1,number+1):
    star = star + "*"
    print(star)