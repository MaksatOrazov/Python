# -*- coding: utf-8 -*-
"""
Created on Wed May 10 00:59:55 2023

@author: pc
"""

sayilar = [1,2,4,5,7]

sayilarFiltreli = list(filter(lambda sayi: sayi>2,sayilar)) #sayilari filtrelemek icin kullanilir
print(sayilarFiltreli)