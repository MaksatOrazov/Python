# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 22:34:29 2023

@author: pc
"""
#%% Example - 1
x = int(input("Enter X : "))
y = int(input("Enter Y : "))

if x > 0:
    if y > 0:
        print("Area 1")
    else:
        print("Area 4")
else:
    if y > 0:
        print("Area 2")
    else:
        print("Area 3")
#%% Example - 2

number = int(input("Enter Number : ")) 
a = number // 100
b = number // 10 % 10
c = number % 10

if(a + b + c) % 2 == 0:
    print("Even number")
else:
    print("Single number")

#%% Example - 3

number1 = int(input("Number 1 : "))
number2 = int(input("Number 2 : "))        
number3 = int(input("Number 3 : "))        
number4 = int(input("Number 4 : "))        

if (number1 + number2) % 2 == (number3 + number4) % 2:
    print("Same")
else:
    print("Different")
    
#%% Example - 4

a = int(input("Number 1 : "))
b = int(input("Number 2 : "))
c = int(input("Number 3 : "))

if a + b > c and a + c > b and b + c > a:
    print("It is triangle")
else:
    print("It is not triangle")
    
#%% Example - 5

n = int(input())
m = int(input())
k = int(input())

if (k % n == 0 or k % m == 0) and (k < n * m):
    print("Yes")
else:
    print("No")
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        