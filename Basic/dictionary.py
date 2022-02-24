# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 15:26:34 2022

@author: My Computer
"""
# 1st choise
dictionary = { 
                "book" : "kitap",
                "table" : "masa"
            }

dictionary["book"] = "kitap 1"
dictionary["pencil"] = "kalem"
del dictionary["book"]
print(len(dictionary))
print(dictionary)
print("-----------------------------------------------")
# 2nd choise

dictionary2 = dict(kitap = "book", masa = "table")
print(dictionary2)
