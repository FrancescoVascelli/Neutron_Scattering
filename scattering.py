# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 15:58:08 2022

@author: Francesco Vascelli
"""

import time
from numpy import random
from rich.progress import track
import init
import utility



class VectorXY:
    """
    Vector_XY interface
    """

    def __init__(self, old_x: int = 0, old_y: int = 0, new_x: int = 0, new_y: int = 0):
        self.old_x = old_x
        self.old_y = old_y
        self.new_x = new_x
        self.new_y = new_y


vector_xy: VectorXY = VectorXY()


class RandomWalk:
    """
     RandomWalk interface is used as temporary place to store
     value of `back`, `lost` and `through` neutrons
    """
    def __init__(self, back: int = 0, lost: int = 0, through: int = 0):
        self.back = back
        self.lost = lost
        self.through = through

random_walk: RandomWalk = RandomWalk()

class RandomWalkResult:
    """
     RandomWalkResult interface is use to collect al `RandomWalk` result in order to output them
    """
    def __init__(self, arr_depth: list, arr_back: list, arr_lost: list, arr_through: list):
        self.arr_depth = arr_depth
        self.arr_back = arr_back
        self.arr_lost = arr_lost
        self.arr_through = arr_through

random_walk_result: RandomWalkResult = RandomWalkResult(arr_depth=[0],arr_back=[0],arr_lost=[0],arr_through=[0])

def compute_random_walk(n_particles: int, depth: int, steps: int):
    """
    This method call `random_walk_2d` for `n_particles` times.
    """
    for i in range(n_particles):
        t_start = time.perf_counter_ns()
        random_walk_2d(depth=depth, steps=steps)
        t_end = time.perf_counter_ns()
        utility.execute_debug(utility.execution_time_message,
                             f'Random Walk Depth:[{depth}/{init.params.max_depth}] - Particles:[{i}/{n_particles}] takes', t_start, t_end, init.messageType.MESSAGE_TYPE_DEBUG)

def scatter(n_particles: int, steps: int, max_depth: int):
    """
    This method collects all the result of the `random_walk` object and append them
    to a `random_walk_result` object in order to output data
    and use them in metod `utility.graph_plot` to create the graph
    """
    t_start = time.perf_counter()
    for depth in track(range(init.constants.MIN_DEPTH, max_depth), description="⚛️  The particles is moving ...", refresh_per_second=init.params.refresh_per_second):
        compute_random_walk(
            n_particles=n_particles, depth=depth, steps=steps)
        random_walk_result.arr_depth.append(depth)
        random_walk_result.arr_back.append(random_walk.back/n_particles)
        random_walk_result.arr_lost.append(random_walk.lost/n_particles)
        random_walk_result.arr_through.append(random_walk.through/n_particles)
        random_walk.back = 0
        random_walk.lost = 0
        random_walk.through = 0
    t_end = time.perf_counter()
    utility.execute_debug(utility.execution_time_message, 'Scatter execution time',
                         t_start, t_end, init.messageType.MESSAGE_TYPE_DEBUG)
    return random_walk_result


def random_walk_2d(depth: int, steps: int):
    """
    This method performs a random walk in 2D for a neutron.

    Parameters
        depth : width of the reactor wall in units of mean free path
        steps : number of interactions before the neutron stops

    """
    # The neutron starts inside the reactor wall towards the positive x-axis.
    vector_xy.old_x = 0
    vector_xy.old_y = 0
    vector_xy.new_x = 1
    vector_xy.new_y = 0
    depth_plus_one = depth+1
    for _ in range(steps):
        random_number = random.rand()
        # The probability of going forward is double with respect to changing direction.
        if random_number < init.constants.ONE_SIX:
            turn_right()
        if random_number >= init.constants.ONE_SIX and random_number < init.constants.ONE_TREE:
            turn_left()
        if random_number >= init.constants.ONE_TREE:
            go_forward()
        # Stop the random walk if the neutron goes all the way through the reactor wall.
        if vector_xy.new_x == depth_plus_one:
            random_walk.through += 1
            break
        # Stop the random walk if the neutron returns inside the reactor.
        if vector_xy.new_x == -1:
            random_walk.back += 1
            break
    # Otherwise, the neutron is lost inside the reactor wall.
    else:
        random_walk.lost += 1


def turn_left():
    """
    This method changes the direction of the neutron to the left
    and takes a step of the random walk.
    """
    # The neutron has +x direction
    if vector_xy.new_x-vector_xy.old_x == 1:

        vector_xy.old_x += 1
        vector_xy.new_y += 1
    # The neutron has -x direction
    elif vector_xy.new_x-vector_xy.old_x == -1:

        vector_xy.new_x += 1
        vector_xy.new_y -= 1
    # The neutron has +y direction
    elif vector_xy.new_y-vector_xy.old_y == 1:
        vector_xy.old_y += 1
        vector_xy.new_x -= 1
    # The neutron has -y direction
    elif vector_xy.new_y-vector_xy.old_y == -1:

        vector_xy.new_x += 1
        vector_xy.new_y += 1


def turn_right():
    """
    This method changes the direction of the neutron to the right
    and takes a step of the random walk.
    """
    # The neutron has +x direction
    if vector_xy.new_x-vector_xy.old_x == 1:

        vector_xy.old_x += 1
        vector_xy.new_y -= 1
    # The neutron has -x direction
    elif vector_xy.new_x-vector_xy.old_x == -1:

        vector_xy.new_x += 1
        vector_xy.new_y += 1
    # The neutron has +y direction
    elif vector_xy.new_y-vector_xy.old_y == 1:
        vector_xy.old_y += 1
        vector_xy.new_x += 1
    # The neutron has -y direction
    elif vector_xy.new_y-vector_xy.old_y == -1:

        vector_xy.new_x -= 1
        vector_xy.new_y += 1


def go_forward():
    """
    This method makes a step of the random walk in the same direction.
    """
    # The neutron has +x direction
    if vector_xy.new_x-vector_xy.old_x == 1:

        vector_xy.old_x += 1
        vector_xy.new_x += 1
    # The neutron has -x direction
    elif vector_xy.new_x-vector_xy.old_x == -1:

        vector_xy.old_x -= 1
        vector_xy.new_x -= 1
    # The neutron has +y direction
    elif vector_xy.new_y-vector_xy.old_y == 1:

        vector_xy.old_y += 1
        vector_xy.new_y += 1
    # The neutron has -y direction
    elif vector_xy.new_y-vector_xy.old_y == -1:

        vector_xy.old_y -= 1
        vector_xy.new_y -= 1
