# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 22:23:15 2022

@author: My Computer
"""
message = "Hello World"

print(message[4])
print(message[0:5])
print(len(message))

#Len
newMessage = message[len(message)-1 : len(message)]
print(newMessage)

#Lower/Upper

print(message.lower())
print(message.upper())

#Replace

print(message.replace("e", "a"))

# Split/ Strip

info = "Maksat;Orazov;25;Balikesir"
print(info.split(";"))

#input
name = input("name : ")
number1 = input("1st number : ")
number2 = input("2nd number : ")
print(int(number1) + int(number2))