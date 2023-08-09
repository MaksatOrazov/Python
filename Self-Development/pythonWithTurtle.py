# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 11:45:02 2023

@author: pc
"""

import turtle
import random

def square(a):
    for i in range(4):
        arrow.color(random.choice(colors))
        #arrow.color(colors[i])
        arrow.forward(a)
        arrow.left(90)

colors = ["red","yellow","black","purple","green","blue"]
        
arrow = turtle.Turtle()
arrow.speed(0)

border = 5
for i in range(100):
    
    square(border)
    border = border + 5
    arrow.right(5)
