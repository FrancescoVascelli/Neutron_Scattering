# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 10:28:34 2022

@author: Francesco Vascelli
"""

import scattering
import numpy as np
from numpy import random
import configparser

import os
import sys
from sys import argv

config = configparser.ConfigParser()
config.read(sys.argv[1])

os.makedirs('./data',exist_ok=True)
os.makedirs('./images',exist_ok=True)
destination0 = config.get('paths','n_back')
destination1 = config.get('paths','n_lost')
destination2 = config.get('paths','n_through')
destination3 = config.get('paths','depth')

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


steps=100

x=[]
y0=[]
y1=[]
y2=[]
for depth in range(2,80):
    for j in range(n_particles):   
        xy_vector = [0,0,1,0]
        scattering.random_walk(xy_vector, n_end, depth, steps)
    x.append(depth)
    y0.append(n_end[0]/n_particles)
    y1.append(n_end[1]/n_particles)
    y2.append(n_end[2]/n_particles)
    n_end = [0,0,0]
    

    
np.save(destination0,y0)
np.save(destination1,y1)
np.save(destination2,y2)

np.save(destination3,x)
    




