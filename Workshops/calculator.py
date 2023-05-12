# -*- coding: utf-8 -*-
"""
Created on Fri May  5 10:54:35 2023

@author: pc
"""
def topla(sayi1,sayi2):
    return sayi1 + sayi2
def cikar(sayi1,sayi2):
    return sayi1 - sayi2
def carp(sayi1,sayi2):
    return sayi1 * sayi2
def bol(sayi1,sayi2):
    return sayi1 / sayi2

print("Operasyon : ")
print("1 : Topla")
print("2 : Cikar")
print("3 : Carp")
print("4 : Bol")


sayi1 = int(input("Sayi 1 : "))
sayi2 = int(input("Sayi 2 : "))
secenek = int(input("Secenek : "))


if secenek == 1:
    print("Toplam = " + str(topla(sayi1, sayi2)))
elif secenek == 2:
    print("Cikarma = " + str(cikar(sayi1, sayi2)))
elif secenek == 3:
    print("Carpma = " + str(carp(sayi1, sayi2)))
elif secenek == 4:
    print("Bolme = " + str(bol(sayi1, sayi2)))
else:
    print("Yanlis secenek!")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    