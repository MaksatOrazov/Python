# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 14:35:52 2023

@author: pc
"""

import turtle

screen = turtle.Screen()

screen.bgcolor("cyan")
screen.setup(700,700)

arrow = turtle.Turtle()
arrow.color("red")
arrow.goto(0,200)
arrow.goto(100,100)
arrow.goto(180,200)
arrow.goto(180,0)




turtle.mainloop()