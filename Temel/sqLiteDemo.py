# -*- coding: utf-8 -*-
"""
Created on Mon May  8 02:38:45 2023

@author: pc
"""

import sqlite3
#def selectOperations():
    #connection = sqlite3.connect("chinook.db")
    #%%
    # cursor = connection.execute("""select FirstName,LastName from customers 
    #                             where city='Prague' or city = 'Berlin'
    #                             order by FirstName,LastName desc""")
    
    # for row in cursor:
    #     print("First Name = " + row[0])
    #     print("Last Name = " + row[1])
    #     print("***********************")
    #
    #%%
    # cursor = connection.execute("""select city,count(*) from Customers group by city 
    #                             having count(*) > 1 order by city""")
    
    # for row in cursor:
    #     print("City = " + str(row[0]))
    #     print("count = " + str(row[1]))
    #     print("***********************")
    #%%
    
    # cursor = connection.execute("""select FirstName,LastName from customers 
    #                              where FirstName like 'a%' """)
    
    # for row in cursor:
    #      print("First Name = " + row[0])
    #      print("Last Name = " + row[1])
    #      print("***********************")
         
    #connection.close()

#selectOperations()
#%%
# def insertcustomer():
#     connection = sqlite3.connect("chinook.db")
#     connection.execute("""insert into customers (firstName,lastName,city,email) 
#                        values('Maxi','Orazov','Tbilisi','maxi.orazov96@gmail.com')""")
#     connection.commit()
#     connection.close()                   
    
# insertcustomer()
#%%
# def updateCustomer():
#     connection = sqlite3.connect("chinook.db")
#     connection.execute("""update customers set city='Balikesir' 
#                        where city = 'Tbilisi' """)
    
#     connection.commit()
#     connection.close()
# updateCustomer()
#%%
# def deleteCustomer():
#     connection = sqlite3.connect("chinook.db")
#     connection.execute("""delete from customers where city='Balikesir' """)
    
#     connection.commit()
#     connection.close()
# deleteCustomer()    
#%%
def joinOperations():
    connection =sqlite3.connect("chinook.db")
    cursor = connection.execute("""select albums.Title,artists.Name from artists
                                inner join albums on artists.ArtistId = albums.ArtistId""")
    
    for row in cursor:
        print("Title = " + row[0] + " Name = " + row[1])
        print("***************************************")
        
    connection.close()
joinOperations()


























