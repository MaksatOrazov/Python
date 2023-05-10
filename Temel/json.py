# -*- coding: utf-8 -*-
"""
Created on Mon May  8 02:00:15 2023

@author: pc
"""
import json

data = '{"firstName":"Maxi","lastName":"Orazov"}'

y = json.loads(data)
print(y["firstName"])
print(y["lastName"])

customer = {
    "fistName":"Maxi",
    "email":"maxi.orazov96@gmail.com"
    
    }

customerJson = json.dumps(customer)
print(customer)

print(json.dumps("Maxi"))









































