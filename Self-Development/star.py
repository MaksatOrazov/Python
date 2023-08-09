# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 14:18:37 2023

@author: pc
"""

import turtle
import random

#------------Star Options--------------------------------------------
def star():
    arrow.begin_fill()
    size = random.randint(10, 100)
    for i in range(5):
        arrow.forward(size)
        arrow.right(144)
    arrow.end_fill()
#------------------Screen Options----------------------------------
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(700,500)


arrow = turtle.Turtle()

colors = ["red","white","purple","green","yellow","pink","orange","blue","cyan","lime"]

for i in range(10):
    x = random.randint(-300, 300)
    y = random.randint(-200, 200)
    arrow.penup()
    arrow.setposition(x,y)
    arrow.color(colors[i])
    arrow.pendown()
    star()


turtle.mainloop()