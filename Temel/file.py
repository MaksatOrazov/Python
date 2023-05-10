# -*- coding: utf-8 -*-
"""
Created on Mon May  8 01:39:43 2023

@author: pc
"""
#%%
f = open("customers.txt") # r=read, a=append x=create, w=write

#print(f.read())  #Tumunu okur
print("****************")
#print(f.readline())  #Satir satir okur
for l in f:           #dongude kullanmak
    print(l)


f.close()
#%%
#%%
fileToAppend = open("students.txt","a")

fileToAppend.write("Maxi")  #isim eklemek icin

fileToAppend.close()

# import os     #dosya silmek icin kullaniriz
# os.remove("students.txt")
#%%