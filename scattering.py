# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 15:58:08 2022

@author: Francesco Vascelli
"""

import numpy 
from numpy import random

def random_walk(n_end, depth, steps):
    xy_vector = [0,0,1,0]
    for i in range(steps):
        p = random.rand()
    
        if p<float(1/6):
            turn_right(xy_vector)
        if p>=float(1/6) and p<float(1/3):
              turn_left(xy_vector)
        if p>=float(1/3):
            go_forward(xy_vector)
                          
        if xy_vector[2]==(depth+1):
            n_end[2]+=1
            break
        if xy_vector[2]==-1:
            n_end[0]+=1
            break
    else:
        n_end[1]+=1
    

def turn_left(xy_vector):
    if xy_vector[2]-xy_vector[0]==1: #+x direction
    
        xy_vector[0] += 1
        xy_vector[3] += 1
        
    if xy_vector[2]-xy_vector[0]==-1: #-x direction
        
        xy_vector[2] += 1
        xy_vector[3] -= 1
        
    if xy_vector[3]-xy_vector[1]==1: #+y direction
        xy_vector[1] += 1
        xy_vector[2] -= 1
        
    if xy_vector[3]-xy_vector[1]==-1: #-y direction
        
        xy_vector[2] += 1
        xy_vector[3] += 1   
        
   
def turn_right(xy_vector):
    if xy_vector[2]-xy_vector[0]==1: #+x direction
    
        xy_vector[0] += 1
        xy_vector[3] -= 1
        
    if xy_vector[2]-xy_vector[0]==-1: #-x direction
        
        xy_vector[2] += 1
        xy_vector[3] += 1
        
    if xy_vector[3]-xy_vector[1]==1: #+y direction
        xy_vector[1] += 1
        xy_vector[2] += 1
        
    if xy_vector[3]-xy_vector[1]==-1: #-y direction
        
        xy_vector[2] -= 1
        xy_vector[3] += 1   
        

def go_forward(xy_vector):
    if xy_vector[2]-xy_vector[0]==1:  #+x direction
        
        xy_vector[0] += 1
        xy_vector[2] += 1
        
    if xy_vector[2]-xy_vector[0]==-1: #-x direction
        
        xy_vector[0] -= 1
        xy_vector[2] -= 1
        
    if xy_vector[3]-xy_vector[1]==1: #+y direction
        
        xy_vector[1] += 1 
        xy_vector[3] += 1
        
    if xy_vector[3]-xy_vector[1]==-1: #-y direction
        
        xy_vector[1] -= 1
        xy_vector[3] -= 1
        