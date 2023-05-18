# -*- coding: utf-8 -*-
"""
Created on Tue May 16 07:19:04 2023

@author: pc
"""

import time

def animate_heart():
    heart_frames = [
        '''
    ***        ***  
  *****      ***** 
*******    *******
*******    *******
  *****      ***** 
    ***        ***  
      *          ''',
        '''
    ***        ***  
  *****      ***** 
*******    *******
********  ********
  *******  ******* 
    *****  *****   
      ***  ***     ''',
        '''
    ***        ***  
  *****      ***** 
*******    *******
*************** 
  *************   
    *********     
      *******     ''',
        '''
    ***        ***  
  *****      ***** 
*******    *******
*************    
  ***********     
    *********     
      *******     ''',
        '''
    ***        ***  
  *****      ***** 
*******    *******
*************    
  ***********     
    *********     
      *******     ''',
        '''
    ***        ***  
  *****      ***** 
*******    *******
*************** 
  *************   
    *********     
      *******     ''',
        '''
    ***        ***  
  *****      ***** 
*******    *******
********  ********
  *******  ******* 
    *****  *****   
      ***  ***     ''',
        '''
    ***        ***  
  *****      ***** 
*******    *******
*******    *******
  *****      ***** 
    ***        ***  
      *          '''
    ]

    while True:
        for frame in heart_frames:
            print(frame)
            time.sleep(0.3)
            # Ekranı temizle
            print("\033c")

animate_heart()