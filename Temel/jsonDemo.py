# -*- coding: utf-8 -*-
"""
Created on Mon May  8 02:10:18 2023

@author: pc
"""

import json

with open("users.json") as users:
    data = json.load(users)
    for x in range(6):
        print(data[x]["username"])
        print(data[x]["email"])
        print(data[x]["address"]["street"])
        print(data[x]["address"]["geo"]["lat"])
        print("*****************************")
    
    