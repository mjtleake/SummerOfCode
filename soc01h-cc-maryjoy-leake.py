# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 15:20:32 2018

@author: Mary
"""

import random 

def world_generator():
    """Generates the continent where X refers to land and O refers to water.
    
    """    
    grid = []
    for row in range(0,11):
        row = []
        for i in range(0,11):
            x = random.choice([0, 1])
            row.append(x)
        print(row)
        grid.append(row)
    
world_generator()
"""
def your_position():
    #Generates your initial position in your world. 
    row = random.choice([x for x in range(0,12)])
    col = random.choice([x for x in range(0,12)])
    print("(row,col) = (" + str(row) + ", " + str(col) + ")")
    
your_position()

"""