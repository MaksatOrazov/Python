# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 03:35:24 2023

@author: pc
"""

sentence = "bugun hava cok guzel"

words = sentence.split()
words.sort()

for word in words:
    print(word)