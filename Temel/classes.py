# -*- coding: utf-8 -*-
"""
Created on Fri May  5 10:08:08 2023

@author: pc
"""
class Matematik:
    def __init__(self,sayi1,sayi2):
        self.sayi1 = sayi1
        self.sayi2 = sayi2 
    def topla(self):
        return self.sayi1 + self.sayi2
    
    def cikar(self):
        return self.sayi1 - self.sayi2
    
    def carp(self):
        return self.sayi1 * self.sayi2
    
    def bol(self):
        return self.sayi1 / self.sayi2
    
    
matematik = Matematik(2,45)
matematik2 = Matematik(6,45)
print("Toplam = " + str(matematik.topla()))
print("Cikarma = " + str(matematik2.cikar()))