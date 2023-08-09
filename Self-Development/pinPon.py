# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 17:02:24 2023

@author: pc
"""

import turtle

#---------------Screen Options---------------------
screen = turtle.Screen()
screen.title("PingPong")
screen.bgcolor("lime")
screen.setup(800,600)
screen.tracer(0)

#---------------Point Options---------------

writing = turtle.Turtle()
writing.speed(0)
writing.color("purple")
writing.penup()
writing.goto(0,260)
writing.write("Player A:0   Player B:0",align="center",font=("Courier",24,"bold"))
writing.hideturtle()

point_a = 0
point_b = 0
#-----------Rocket Options-----------------------

rocket_a = turtle.Turtle()
rocket_a.speed(0)
rocket_a.shape("square")
rocket_a.color("red")
rocket_a.penup()
rocket_a.goto(-350,0)
rocket_a.shapesize(5,1)

rocket_b = turtle.Turtle()
rocket_b.speed(0)
rocket_b.shape("square")
rocket_b.color("red")
rocket_b.penup()
rocket_b.goto(350,0)
rocket_b.shapesize(5,1)

#--------------Ball Options------------------------------

ball = turtle.Turtle()

ball.speed(0)
ball.shape("circle")
ball.color("blue")
ball.penup()
ball.dx = 0.15
ball.dy = 0.15


#------------------------Keyboard Options--------------
def rocket_a_up():
    y = rocket_a.ycor()
    y = y + 20
    rocket_a.sety(y)
    
def rocket_a_down():
    y = rocket_a.ycor()
    y = y - 20
    rocket_a.sety(y)
    
def rocket_b_up():
    y = rocket_b.ycor()
    y = y + 20
    rocket_b.sety(y)
    
def rocket_b_down():
    y = rocket_b.ycor()
    y = y - 20
    rocket_b.sety(y)

screen.listen()
screen.onkeypress(rocket_a_up, "w")
screen.onkeypress(rocket_a_down,"s")
screen.onkeypress(rocket_b_up, "Up")
screen.onkeypress(rocket_b_down,"Down")


#----------------Run Options---------------------------

while True:
    screen.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy) 
    
    if ball.ycor()>290 or ball.ycor()<-290:
        ball.dy = ball.dy * -1
        
    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx = ball.dx * -1
        point_a = point_a + 1
        writing.clear()
        writing.write("Player A:{}  Player B:{}".format(point_a,point_b),align="center",font=("Courier",24,"bold"))
    
    if ball.xcor()< -390:
        ball.goto(0,0)
        ball.dx = ball.dx * -1
        point_b = point_b + 1
        writing.clear()
        writing.write("Player A:{}   Player B:{}".format(point_a,point_b),align="center",font=("Courier",24,"bold"))
        
    if (ball.xcor()>340 and ball.xcor()<350) and (ball.ycor()<rocket_b.ycor()+60 and ball.ycor()> rocket_b.ycor()-60):
        ball.setx(340)
        ball.dx = ball.dx * -1
        
    
    if (ball.xcor()< -340 and ball.xcor()>-350) and (ball.ycor()<rocket_a.ycor()+60 and ball.ycor()> rocket_a.ycor()-60):
        ball.setx(-340)
        ball.dx = ball.dx * -1
        
    




























