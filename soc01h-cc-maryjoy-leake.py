# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 15:20:32 2018

@author: Mary
"""

import random 

def world_generator():
    #Generates the continent where X refers to land and O refers to water.
        
        
    for row in range(0,11):
        grid = []
        for i in range(0,11):
            x = random.choice([0, 1])
            grid.append(x)
        print(grid)
        

world_generator()