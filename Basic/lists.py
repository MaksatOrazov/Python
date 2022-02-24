# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 23:13:40 2022

@author: My Computer
"""

students = ["Maksat", "Duygu", "Nasir"]

print(students[1])
students.append("Enes")
students.remove("Nasir")
students[2] = "Efe"
print(len(students))

#Other functions

print("Count of Maksat = " + str(students.count("Maksat")))
print("Index of Maksat = " + str(students.index("Maksat")))
students.pop(2)
students.insert(2, "Secil")
students.reverse()
print(students)


# students2 = students
# students2[0] = "Enes"
# print(students2)