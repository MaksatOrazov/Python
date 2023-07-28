# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 06:43:33 2023

@author: pc
"""
nt = int(input("0-100 araasi bir not giriniz: "))

if nt>100 and nt<0:
    print("Error! Not 0-100 arasinda olmali.")
elif 100>=nt>=90:
    print("AA")
elif 90>nt>=80:
    print("BA")
elif 80>nt>=70:
    print("BB")
elif 70>nt>=60:
    print("CC")
elif 60>nt>=50:
    print("DD")
elif 50>nt>=0:
    print("FF")
else:
    print("Error! Not 0-100 arasinda olmali.")