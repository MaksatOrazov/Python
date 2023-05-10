# -*- coding: utf-8 -*-
"""
Created on Mon May  8 01:56:30 2023

@author: pc
"""

students = ["Maxi","Duygu","Ela","Efe"]

fileToAppend = open("students2.txt","a")
for student in students:
    fileToAppend.write(student)
    fileToAppend.write("\n")
    
fileToAppend.close()