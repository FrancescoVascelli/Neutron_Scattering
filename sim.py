# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 10:28:34 2022

@author: Francesco Vascelli
"""

import scattering
import numpy 
from numpy import random


#initial conditions 
old_x=0
old_y=0

new_x=1 
new_y=0


xy_vector = [old_x,old_y,new_x,new_y]

n_particles=1000

n_back=0
n_lost=0
n_through=0

n_end = [n_back,n_lost,n_through]


depth=50

steps=100




for j in range(n_particles):   
    xy_vector = [0,0,1,0]
    scattering.random_walk(xy_vector, n_end, depth, steps)


print(n_end)
    




