# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 14:23:59 2022

@author: Francesco Vascelli
"""

from hypothesis import strategies as st
from hypothesis import settings
from hypothesis import given
import scattering
import init

def test_random_walk_2d(depth, steps):
    """
    Do a random walk for a single particle for any number of depth and steps
    """
    scattering.random_walk.back = 0
    scattering.random_walk.lost = 0
    scattering.random_walk.through = 0
    scattering.random_walk_2d(depth=depth, steps=steps)
    # Test if its destination is in compute
    assert sum((scattering.random_walk.back, scattering.random_walk.lost,
               scattering.random_walk.through)) == 1

def test_turn_right():
    """
    Turn a particle, with +x direction, to the right
    """
    scattering.vector_xy.old_x = 0
    scattering.vector_xy.old_y = 0
    scattering.vector_xy.new_x = 1
    scattering.vector_xy.new_y = 0
    scattering.turn_right()
    # Test if the particle correctly turned to the rigth
    assert scattering.vector_xy.old_x == 1
    assert scattering.vector_xy.old_y == 0
    assert scattering.vector_xy.new_x == 1
    assert scattering.vector_xy.new_y == -1

def test_turn_left():
    """
    Turn a particle, with +x direction, to the left
    """
    scattering.vector_xy.old_x = 0
    scattering.vector_xy.old_y = 0
    scattering.vector_xy.new_x = 1
    scattering.vector_xy.new_y = 0
    scattering.turn_left()
    # Test if the particle correctly turned to the left
    assert scattering.vector_xy.old_x == 1
    assert scattering.vector_xy.old_y == 0
    assert scattering.vector_xy.new_x == 1
    assert scattering.vector_xy.new_y == 1

def test_go_forward():
    """
    Make a particle, with +x direction, go forward
    """
    scattering.vector_xy.old_x = 0
    scattering.vector_xy.old_y = 0
    scattering.vector_xy.new_x = 1
    scattering.vector_xy.new_y = 0
    scattering.go_forward()
    # Test if the particle correctly goes in the same direction
    assert scattering.vector_xy.old_x == 1
    assert scattering.vector_xy.old_y == 0
    assert scattering.vector_xy.new_x == 2
    assert scattering.vector_xy.new_y == 0

@given(depth=st.integers(1, 80), steps=st.integers(1, 100))
@settings(max_examples=1)
def test_all_suite(depth,steps):
    """
    Execute all test suite
    """
    try:
        test_random_walk_2d(depth,steps)
        test_turn_right()
        test_turn_left()
        test_go_forward()
    except AssertionError:
        init.console_print(message="🧪❌  Errors in tests suite !")
    else:
        init.console_print(message="🧪👍  All tests suite are OK !")
    finally:
        init.console_print(message="🧪  Test suite are completed !")
