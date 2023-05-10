# -*- coding: utf-8 -*-
"""
Created on Mon May  8 03:31:45 2023

@author: pc
"""
try:
    sayi = int(input("Sayi giriniz : "))
except ValueError:
    print("Tip uyusmazligi. Lutfen sayi giriniz!")
except ZeroDivisionError:
    print("Payda sifir olamaz!")
except:
    print("Bir hata olustu")
    
print("bitti")