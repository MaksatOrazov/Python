# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 20:13:40 2023

@author: pc
"""

students = ["Maxi", "Jeyhun", "Dotde"]

print(students)
print(len(students))
students.append("Kichi")
students[2] = "Ahmet"
print(students[0])
#print(students.clear())
print("Maxi ismi = " + str(students.count("Maxi")))
print("Maxi indexi = " + str(students.index("Maxi")))
students.pop(2)
students.insert(1,"Ahmet")
students.reverse()
print(students)
students3 = students.copy()
students2 = students

students2[0] = "Mekan"
students.sort()
print(students)
print(students3)

