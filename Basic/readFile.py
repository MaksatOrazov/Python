# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 18:13:42 2022

@author: My Computer
"""
# r=read, a=append, w=write, x=create

f = open("customers.txt")
#print(f.read())      #---> reads all text.

for l in f:    # ---> reads line by line
    print(l)


