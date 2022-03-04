# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 11:33:24 2022

@author: My Computer
"""
import sqlite3
connection = sqlite3.connect("chinook.db")

# cursor = connection.execute("""select Firstname,Lastname from customers 
#                             where city = 'Prague' or city = 'Berlin'
#                             order by Firstname desc""")

# for row in cursor:
#     print("Firstname : " + row[0])
#     print("Last Name : " + row[1])
#     print("----------------------")
#------------------------------------------------------------------------------


cursor = connection.execute("""select city,count(*) from Customers group by city 
                            having count(*)>1 order by city""")
for row in cursor:
   print("City : " + row[0])
   print("Count : " + str(row[1]))
   print("-----------------------")

connection.close()