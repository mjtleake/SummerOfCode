# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 15:20:32 2018

@author: Mary
"""

import random 
import numpy as np


def world_generator(n):
    #Generates the continent where 1 refers to land and 0 refers to water.  
    grid = []
    for row in range(0,n):
        row = []
        for i in range(0,n):
            x = random.choice([0, 1])
            row.append(x)
        grid.append(row)
    return grid


def your_position(n):
    #Generates the coordinates of your initial position in your world. 
    grid_arr = np.array(grid)
    r = random.randrange(0,n)
    c = random.randrange(0,n)
    row, col = r, c
    if grid_arr[row][col] == 1:
        print(grid_arr)
        initial_position = (row, col)
        print("You are standing at location (row, col): ", initial_position)
        return initial_position
    else:
        your_position(n)

   
def total_continent_count():
    #Counts the total land continent. 
    count = 0
    for row in grid:
        for col in row:
            if col == 1:
                count += 1
    return count
            

def check_next_continent():
    #Checks if the next tile of land is reachable
    row = initial_position[0]
    col = initial_position[1]
    print(row)
    #continent_taken = [initial_position]
    grid_arr = np.array(grid)
    #grid_arr[row][col] = 'X'
    #print(grid_arr)

world_size = 11
grid = world_generator(world_size) 
initial_position = your_position(world_size)
print("Total continent count: ", total_continent_count())
check_next_continent()