# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 19:24:52 2023

@author: pc
"""
#Substring
message = "Hello World"

print(message)
print(len(message))
print(message[2])
print(message[6:len(message)])
newMessage = message[6:len(message)]
print(newMessage)
newMessage2 = message[len(message)-1:len(message)]
print(newMessage2)


#Lower/Upper
print(message.lower())
print(message.upper())

#replace
print(message.replace("o","a"))

#split
info = "Maxi;Orazov;26;Bayramali"
print(info.split())
print("Age = " + info.split(";")[2])

#input

name = input("Name : ")
number1 = input("Number1 : ")
number2 = input("Number2 : ")
print(int(number1) + int(number2))