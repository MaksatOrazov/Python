# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 17:00:56 2022

@author: My Computer
"""

import json

with open("users.json") as users:
    data = json.load(users)
    for x in range(5):
        print(data[x]["username"])
        print(data[x]["email"])
        print(data[x]["address"]["street"])
        print("-----------------------------")