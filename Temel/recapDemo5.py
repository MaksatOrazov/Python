# -*- coding: utf-8 -*-
"""
Created on Tue May  9 11:03:00 2023

@author: pc
"""
import sys
liste = ['Maxi',0,3,"6"]

for x in liste:
    try:
        print("Sayi: " + str(x))
        sonuc = 1/int(x)
        print("Sonuc = " + str(sonuc))
    except ValueError:
            print(str(x)+ " bir sayi degil")
    except ZeroDivisionError:
        print(str(x)+ " icin sifira bolme hatasi")
    except:
        print(str(x) + " Hesaplanamadi")
        print("System diyor ki: "+ str(sys.exc_info()[0]))
    finally:
        print("Islemler bitti")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        