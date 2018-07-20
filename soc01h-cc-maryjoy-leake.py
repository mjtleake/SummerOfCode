# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 15:20:32 2018

@author: Mary
"""

import random 
import numpy as np

def world_generator():
    """Generates the continent where 1 refers to land and 0 refers to water.
    
    """    
    grid = []
    for row in range(0,11):
        row = []
        for i in range(0,11):
            x = random.choice([0, 1])
            row.append(x)
        grid.append(row)
    return grid


def your_position():
    grid = world_generator()
    grid_arr = np.array(grid)
    #Generates your initial position in your world. 
    r = random.randrange(0,11)
    c = random.randrange(0,11)
    row, col = r, c
    if grid_arr[row][col] == 1:
        print(grid_arr)
        initial_position = (row, col)
        print("You are standing at coordinates (row, col): ", initial_position)

    else:
        your_position()
   
    
your_position()

