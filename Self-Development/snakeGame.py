# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 16:39:50 2023

@author: pc
"""

import turtle
import time
import random

speed = 0.15

screen = turtle.Screen()
screen.title("Snake Game")
screen.bgcolor("lightgreen")
screen.setup(width=600, height=600)
screen.tracer(0)

head=turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,100)
head.direction = "Stop"

meal=turtle.Turtle()
meal.speed(0)
meal.shape("circle")
meal.color("red")
meal.penup()
meal.goto(0,0)
meal.shapesize(0.80, 0.80)


tails = []
point = 0

write=turtle.Turtle()
write.speed(0)
write.shape("square")
write.color("blue")
write.penup()
write.goto(0,260)
write.hideturtle()
write.write("Point : {}".format(point),align="center",font=("Courier", 24, "normal") )

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
        
def goUp():
    if head.direction != "down":   # eger yon asagi tarafa degilse yukariya git
        head.direction = "up"
        
def goDown():
    if head.direction != "up":      # eger yon yukari tarafa degilse asagiya git
        head.direction = "down"
        
def goRight():
    if head.direction != "left":
        head.direction = "right"
        
def goLeft():
    if head.direction != "right":
        head.direction = "left"
        
screen.listen()
screen.onkey(goUp,"Up")
screen.onkey(goDown,"Down")
screen.onkey(goRight,"Right")
screen.onkey(goLeft,"Left")

while True:
    screen.update()
    
    if head.xcor() > 300 or head.xcor() < -300 or head.ycor() > 300 or head.ycor() < -300:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
        
        
        for tail in tails:
            tail.goto(1000,1000)
        
        tails = []
        point = 0
        write.clear()
        write.write("Point : {}".format(point), align="center",font=("Courier", 24, "normal") )
        
        speed = 0.15
        
        
    if head.distance(meal) < 20:
        x = random.randint(-250,250)
        y = random.randint(-250,250)
        meal.goto(x,y)
        point = point + 10
        write.clear()
        write.write("Point : {}".format(point), align="center",font=("Courier", 24, "normal") )
        
        speed = speed - 0.001
        
        newTail = turtle.Turtle()
        newTail.speed(0)
        newTail.shape("square")
        newTail.color("white")
        newTail.penup()
        tails.append(newTail)
        
    for i in range(len(tails) -1,0,-1):
        x = tails[i - 1].xcor()
        y = tails[i - 1].ycor()
        tails[i].goto(x,y)
            
    if len(tails) > 0:
        x = head.xcor()
        y = head.ycor()
        tails[0].goto(x,y)
    
    move()
    time.sleep(speed)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    