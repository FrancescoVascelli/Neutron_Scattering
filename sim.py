# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 10:28:34 2022

@author: Francesco
"""

import numpy as np
from numpy import random

""""
set initial direction of the neutron
old and new positions help determine the direction
"""
old_x=0
old_y=0

new_x=1 
new_y=0


xy_vector = [old_x,old_y,new_x,new_y]

"""
Create array of possible destination of neutrons

"""
n_back=0
n_lost=0
n_through=0

n_end= [n_back,n_lost,n_through]

d=500


def random_walk(xy_vector):
    for i in range(100):
        p = random.rand()
    
      #  if p<float(1/6):
       #     turn_right(xy_vector)
       # if p>float(1/6) and p<float(1/3):
       #       turn_left(xy_vector)
        if p>float(1/3):
            go_forward(xy_vector)
                          
        if xy_vector[2]==d+1:
            n_end[2]+=1
            break
        if xy_vector[2]==-1:
            n_end[0]+=1
            break
    

def turn_left(xy_vector):
    return 0

def turn_right(xy_vector):
    return 0

def go_forward(xy_vector):
    if xy_vector[2]-xy_vector[0]==1:
        
        xy_vector[0] += 1
        xy_vector[2] += 1
        
    if xy_vector[2]-xy_vector[0]==-1:
        
        xy_vector[0] -= 1
        xy_vector[2] -= 1
        
    if xy_vector[3]-xy_vector[1]==1:
        
        xy_vector[1] += 1 
        xy_vector[3] += 1
        
    if xy_vector[3]-xy_vector[1]==-1:
        
        xy_vector[1] -= 1
        xy_vector[3] -= 1
        
    
random_walk(xy_vector)

print(n_end)
    




