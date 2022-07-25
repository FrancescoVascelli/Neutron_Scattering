# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 10:28:34 2022

@author: Francesco Vascelli
"""

import scattering
import numpy as np

import configparser

import os
import sys

config = configparser.ConfigParser()
config.read(sys.argv[1])

os.makedirs('./data',exist_ok=True)
os.makedirs('./images',exist_ok=True)

destination0 = config.get('paths','n_back')
destination1 = config.get('paths','n_lost')
destination2 = config.get('paths','n_through')
destination3 = config.get('paths','depth')


n_particles = int(config.get('input','n_particles'))
steps = int(config.get('input','steps'))


n_end = [0,0,0]


x_depth=[]
n_back=[]
n_lost=[]
n_through=[]




for depth in range(2,80):
    for j in range(n_particles):   
        scattering.random_walk(n_end, depth, steps)
    x_depth.append(depth)
    n_back.append(n_end[0]/n_particles)
    n_lost.append(n_end[1]/n_particles)
    n_through.append(n_end[2]/n_particles)
    n_end = [0,0,0]
    

    
np.save(destination0,n_back)
np.save(destination1,n_lost)
np.save(destination2,n_through)

np.save(destination3,x_depth)
    




