# -*- coding: utf-8 -*-
"""
Created on Wed May 10 00:06:29 2023

@author: pc
"""

for num in range(10):
    if num < 5:
        continue
    elif num > 8:
        break
    print(num, end=" ")