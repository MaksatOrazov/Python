# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 17:32:18 2022

@author: My Computer
"""
#no index number

studentsSet = {"Maksat", "Duygu", "Secil"}

studentsSet.add("Nasir")
studentsSet.update(["John", "Elia", "Pinar"])
studentsSet.remove("John")
print(len(studentsSet))
print(studentsSet)

for student in studentsSet:
    print(student)
    
if "Maksat" in studentsSet:
    print("In list")
    
studentsSet.clear()

del studentsSet
print(studentsSet)
