# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 13:48:13 2023

@author: pc
"""

import turtle
import random
# --------------------------Screen options ----------------------------------
screen = turtle.Screen()
screen.screensize(600,600)
screen.title("Catch the Turtles")
screen.bgcolor("blue")
screen.bgpic("turtle.gif")
screen.tracer(2)

#--------------------------Point Options--------------------------------------
score = 0
point = turtle.Turtle()
point.speed(0)
point.shape("square")
point.color("white")
point.penup()
point.hideturtle()
point.goto(-350,350)
point.write("Point : {}".format(score), align="center",font=("Courier",24,"normal"))

# --------------------------Player Options ----------------------------------
player = turtle.Turtle()
player.color("white")
player.shape("triangle")
player.shapesize(3)
player.penup()

#------------------------Speed Options----------------------------------------
speed = 1

speedPoint = turtle.Turtle()
speedPoint.speed(0)
speedPoint.shape("square")
speedPoint.color("white")
speedPoint.penup()
speedPoint.hideturtle()
speedPoint.goto(350,350)
speedPoint.write("Speed : {}".format(speed), align="center",font=("Courier",24,"normal"))

# --------------------------Keyboard options --------------------------------
def turnLeft():
    player.left(90)

def turnRight():
    player.right(90)
    
def increaseSpeed():
    global speed
    speed = speed + 1
    speedPoint.clear()
    speedPoint.write("Speed : {}".format(speed), align="center",font=("Courier",24,"normal"))
    
def reduceSpeed():
    global speed
    speed = speed - 1
    speedPoint.clear()
    speedPoint.write("Speed : {}".format(speed), align="center",font=("Courier",24,"normal"))
    
screen.listen()
screen.onkey(turnLeft,"Left")
screen.onkey(turnRight,"Right")
screen.onkey(increaseSpeed, "Up")
screen.onkey(reduceSpeed, "Down")

#-------------------------Target Options --------------------------------------
maxTarget = 5
targets = []
for i in range(maxTarget):
    targets.append(turtle.Turtle()) 
    targets[i].penup()
    targets[i].color("yellow")
    targets[i].shape("turtle")
    targets[i].speed(0)
    targets[i].setposition(random.randint(-450,450), random.randint(-400, 400))




# -------------------Player and Targets Motion On screen----------------------------------
while True:
    player.forward(speed)
    
    if player.xcor() > 400 or player.xcor() < -400:
        player.right(180)
    if player.ycor() > 400 or player.ycor() < -400:
        player.right(180)
    
    for i in range(maxTarget):
        targets[i].forward(1)
        if targets[i].xcor() > 450 or targets[i].xcor() < -450:
            targets[i].right(random.randint(200, 250))
        if targets[i].ycor() > 450 or targets[i].ycor() < -450:
            targets[i].right(random.randint(200, 250))    
        
        if player.distance(targets[i]) < 40:
            targets[i].setposition(random.randint(-450,450), random.randint(-450, 450))
            targets[i].right(random.randint(0,360))
            score = score + 1
            point.clear()
            point.write("Point : {}".format(score), align="center",font=("Courier",24,"normal"))
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    