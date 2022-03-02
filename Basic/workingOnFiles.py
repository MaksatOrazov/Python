# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 12:48:10 2022

@author: My Computer
"""

fileToAppend = open("students.txt","a")
fileToAppend.write("Maksat")
fileToAppend.close()

import os

if os.path.exists("students.txt"):
   os.remove("students.txt")
else:
    print("no file exists")
