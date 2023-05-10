# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 06:59:33 2023

@author: pc
"""

#degerleri rastgele atiyor.

studentsSet = {"Maxi","Jeyhun","Dotde"}


for student in studentsSet:
    print(student)
    
print("maxi" in studentsSet)
if "Maxi" in studentsSet:
    print("listede var")

studentsSet.add("Ahmet")
studentsSet.update(["Efe","Ege"])
studentsSet.remove("Dotde")
print(studentsSet)