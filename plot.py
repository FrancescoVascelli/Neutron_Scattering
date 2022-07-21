# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 13:57:42 2022

@author: Francesco Vascelli
"""

import numpy as np
import matplotlib.pyplot as plt

import sys
from sys import argv
import configparser

configu = configparser.ConfigParser()
configu.read(sys.argv[1])

source0 = configu.get('paths','n_back')
source1 = configu.get('paths','n_lost')
source2 = configu.get('paths','n_through')
source3 = configu.get('paths','depth')


destination1 = configu.get('paths','ratio_pic')



def graph_plot():
    y0 = np.load(source0)
    y1 = np.load(source1)
    y2 = np.load(source2)
    x = np.load(source3)
    
    f = plt.figure(figsize=(18, 18))
    plt.scatter(x,y0)
    plt.scatter(x,y1)
    plt.scatter(x,y2)

    f.savefig(destination1)
    
    
graph_plot()
