# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 17:35:03 2022

@author: My Computer
"""

sentence = input("Enter the sentence : ")
words = sentence.split()
words.sort()
for word in words:
    print(word)