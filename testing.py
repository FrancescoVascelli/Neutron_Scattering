# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 14:23:59 2022

@author: Francesco Vascelli
"""

import scattering
import numpy as np
import hypothesis
from hypothesis import strategies as st
from hypothesis import settings
from hypothesis import given


@given(depth=st.integers(1,80), steps=st.integers(1, 100))
@settings(max_examples = 1)
def test_random_walk(depth, steps):
    n_end=[0,0,0]
    scattering.random_walk(n_end, depth, steps)
   
    assert sum(n_end) == 1
    

if __name__ == "main":
    pass                
           