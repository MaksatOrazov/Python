from random import randint

#%%
loop = int(input("How many times = "))
total = 0
i = 0

while i < loop:
    number = int(input())
    total = total + number
    i = i + 1
    
print(total)

#%%

number = int(input("Enter the number : "))
counter = 0
while number > 0:
    number = number // 10
    counter = counter + 1
print(counter)

#%%

number = int(input("Enter the number : "))

total = 0

while number > 0:
    x = number % 10
    total = total + x
    number = number // 10
print(total)

#%%

number = int(input("Enter the number : "))
total = 0

while number != 0:
    if number < 0:
        break
    total = total + number
    number = int(input())
else:
    print(total)
    
#%%
number = int(input("Enter the number : "))
i = 1
while i * i <= number:
    print(i * i, end = ' ' )
    i = i + 1

#%%

number = int(input("Enter the number : "))
division = 2

while division <= number:
    if number % division == 0:
        print(division)
        number = number // division
    else:
        division = division + 1
if number > 1:
    print(number)
    
#%%

x = int(input())
y = int(input()) 

day = 1

while x < y:
    x = x + x * 0.1
    day = day + 1
print(day)
        

#%% fibonacci

n = int(input("Number : "))
a = 0
b = 1
i = 2
while i <= n:
    t = b
    b = a + b
    a = t
    i = i + 1
if n == 0:
    b = 0
    
print(b)

























































































