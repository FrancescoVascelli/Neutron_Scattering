# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 13:57:42 2022

@author: Francesco Vascelli
"""

import numpy as np
import matplotlib.pyplot as plt

import sys
import configparser

configu = configparser.ConfigParser()
configu.read(sys.argv[1])

source0 = configu.get('paths','n_back')
source1 = configu.get('paths','n_lost')
source2 = configu.get('paths','n_through')
source3 = configu.get('paths','depth')


destination1 = configu.get('paths','ratio_pic')



def graph_plot():
    

    n_back = np.load(source0)
    n_lost = np.load(source1)
    n_through = np.load(source2)
    x_depth = np.load(source3)
    
    f = plt.figure(figsize=(15, 15))
    
    plt.scatter(x_depth,n_back)
    plt.scatter(x_depth,n_lost)
    plt.scatter(x_depth,n_through)
    
    
    plt.xlabel("Depth (arbitrary units)", fontsize=25)
    plt.ylabel("Ratio of particles", fontsize=25)
    plt.xticks(fontsize=20)
    plt.yticks(np.arange(0.0, 1.0, 0.1), fontsize=20)
    plt.ylim(-0.05,1)
    plt.legend(['back','lost','through'], loc="upper right", fontsize= 20)
    
    f.savefig(destination1)
    plt.show()    
    
graph_plot()
