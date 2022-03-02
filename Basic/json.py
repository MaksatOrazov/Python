# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 13:38:40 2022

@author: My Computer
"""
import json

data = '{"firstName" : "Maksat", "LastName" : "Orazov"}'

y = json.loads(data)
print(y["firstName"])