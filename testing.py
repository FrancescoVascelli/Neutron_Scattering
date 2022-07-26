# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 14:23:59 2022

@author: Francesco Vascelli
"""

import scattering
import hypothesis
from hypothesis import strategies as st
from hypothesis import settings
from hypothesis import given


@given(depth=st.integers(1,80), steps=st.integers(1, 100))
@settings(max_examples = 1)
def test_random_walk(depth, steps):
    #Do a random walk for a single particle for any number of depth and steps
    n_end=[0,0,0]    
    scattering.random_walk(n_end, depth, steps)
    #Test if its destination is in n_end
    assert sum(n_end) == 1


def test_turn_right():
    #Turn a particle, with +x direction, to the right 
    xy_vector = [0,0,1,0]
    scattering.turn_right(xy_vector)
    #Test if the particle correctly turned to the rigth
    assert xy_vector == [1,0,1,-1]

def test_turn_left():
    #Turn a particle, with +x direction, to the left
    xy_vector = [0,0,1,0]
    scattering.turn_left(xy_vector)
    #Test if the particle correctly turned to the left
    assert xy_vector == [1,0,1,1]
    
def test_go_forward():
    #Make a particle, with +x direction, go forward 
    xy_vector = [0,0,1,0]
    scattering.go_forward(xy_vector)
    #Test if the particle correctly goes in the same direction
    assert xy_vector == [1,0,2,0]

    

if __name__ == "main":
    pass                
           