# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 17:25:36 2022

@author: My Computer
"""

x = [[1,2,5],[5,7,3],[8,6,4]]
y = [[9,7,4],[4,6,0],[2,5,1]]

result = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(x)):
    for j in range(len(y)):
        result[i][j] = x[i][j] + y[i][j]
    
print(result)