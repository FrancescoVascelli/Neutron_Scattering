# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 15:58:08 2022

@author: Francesco Vascelli
"""

import numpy
from numpy import random

def random_walk(n_end, depth, steps):
    """This method performs a random walk in 2D for a neutron.
    
    Parameters
        n_end : destination of the neutron [back, lost, through]
        depth : width of the reactor wall in units of mean free path
        steps : number of interactions before the neutron stops
    
    """
    #The neutron starts inside the reactor wall towards the positive x-axis.
    xy_vector = [0,0,1,0]
    for i in range(steps):
        p = random.rand()
        #The probability of going forward is double with respect to changing direction.
        if p<float(1/6):
            turn_right(xy_vector)
        if p>=float(1/6) and p<float(1/3):
              turn_left(xy_vector)
        if p>=float(1/3):
            go_forward(xy_vector)
        
        #Stop the random walk if the neutron goes all the way through the reactor wall.                  
        if xy_vector[2]==(depth+1):
            n_end[2]+=1
            break
        #Stop the random walk if the neutron returns inside the reactor.
        if xy_vector[2]==-1:
            n_end[0]+=1
            break
    #Otherwise, the neutron is lost inside the reactor wall.
    else:
        n_end[1]+=1
    

def turn_left(xy_vector):
    """This method changes the direction of the neutron to the left
    and takes a step of the random walk.
    
    Parameters
       xy_vector : position of the neutron in the xy plane.
                   The first two values are the position in x and y at the previous step,
                   the last two are the current position in x and y 
    """
    #The neutron has +x direction
    if xy_vector[2]-xy_vector[0]==1: 
    
        xy_vector[0] += 1
        xy_vector[3] += 1
    #The neutron has -x direction    
    elif xy_vector[2]-xy_vector[0]==-1: 
        
        xy_vector[2] += 1
        xy_vector[3] -= 1
    #The neutron has +y direction    
    elif xy_vector[3]-xy_vector[1]==1: 
        xy_vector[1] += 1
        xy_vector[2] -= 1
    #The neutron has -y direction    
    elif xy_vector[3]-xy_vector[1]==-1: 
        
        xy_vector[2] += 1
        xy_vector[3] += 1   
        
   
def turn_right(xy_vector):
    """This method changes the direction of the neutron to the right
    and takes a step of the random walk.
    
    Parameters
       xy_vector : position of the neutron in the xy plane.
                   The first two numbers are the position in x and y at the previous step,
                   the last two are the current position in x and y 
    """
    #The neutron has +x direction
    if xy_vector[2]-xy_vector[0]==1: 
    
        xy_vector[0] += 1
        xy_vector[3] -= 1
    #The neutron has -x direction    
    elif xy_vector[2]-xy_vector[0]==-1: 
        
        xy_vector[2] += 1
        xy_vector[3] += 1
    #The neutron has +y direction    
    elif xy_vector[3]-xy_vector[1]==1: 
        xy_vector[1] += 1
        xy_vector[2] += 1
    #The neutron has -y direction    
    elif xy_vector[3]-xy_vector[1]==-1: 
        
        xy_vector[2] -= 1
        xy_vector[3] += 1   
        

def go_forward(xy_vector):
    """This method makes a step of the random walk in the same direction.
    
    Parameters
       xy_vector : position of the neutron in the xy plane.
                   The first two numbers are the position in x and y at the previous step,
                   the last two are the current position in x and y 
    """
    #The neutron has +x direction
    if xy_vector[2]-xy_vector[0]==1:  
        
        xy_vector[0] += 1
        xy_vector[2] += 1
    #The neutron has -x direction    
    elif xy_vector[2]-xy_vector[0]==-1: 
        
        xy_vector[0] -= 1
        xy_vector[2] -= 1
    #The neutron has +y direction    
    elif xy_vector[3]-xy_vector[1]==1:
        
        xy_vector[1] += 1 
        xy_vector[3] += 1
    #The neutron has -y direction    
    elif xy_vector[3]-xy_vector[1]==-1: 
        
        xy_vector[1] -= 1
        xy_vector[3] -= 1
        