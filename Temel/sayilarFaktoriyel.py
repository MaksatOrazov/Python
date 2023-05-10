# -*- coding: utf-8 -*-
"""
Created on Wed May 10 01:03:24 2023

@author: pc
"""

from functools import reduce

sayilar = [1,2,4,6,7,8]
sayilarFaktoriyel = reduce(lambda x,y:x*y,sayilar)# x 1. sayiya y 2. sayiya denk geliyor
                                                  # x 1 iken y 2 oluyor ikisini carpinca sonucu x-e yaziyoruz
                                                 

print(sayilarFaktoriyel)