# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 13:33:11 2022

@author: My Computer
"""

students = ["Maksat", "Duygu", "Secil", "Enes"]

fileToAppend = open("Students.txt","a")

for student in students:
    fileToAppend.write(student)
    fileToAppend.write("\n")
fileToAppend.close()