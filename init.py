# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 10:28:34 2022

@author: Francesco Vascelli
"""
import os
import sys
import argparse
import psutil
from rich.console import Console

console = Console()

class Constants:
    """
    Store all the costants
    """
    def __init__(self):
        self.DEFAULT_GRAPH_OUTPUT = './output/output.png'
        self.DEFAULT_N_PARTICLES = 5000
        self.DEFAULT_STEP = 100
        self.DEFAULT_MAX_DEPTH = 80
        self.DEFAULT_SAVE_DATA = False
        self.DEFAULT_DATA_PATH = "./data"
        self.DEFAULT_GRAPH_ONLY = False
        self.DEFAULT_TESTING = False
        self.DEFAULT_PRINT_GRAPH_CONSOLE = False
        self.DEFAULT_DEBUG = False
        self.DEFAULT_REFRESH_PER_SECOND = 1000
        self.MIN_DEPTH = 2
        self.ONE_SIX = float(1/6)
        self.ONE_TREE = float(1/3)

constants:Constants = Constants()

class MessageType:
    """
    Store all messsage types
    """
    def __init__(self):
        self.MESSAGE_TYPE_NORMAL = 'NORMAL'
        self.MESSAGE_TYPE_DEBUG = 'DEBUG'

messageType:MessageType = MessageType()

class Params:
    """
    List of possible parameters to pass as argument in the program
    """
    def __init__(self, output_graph_path: str = "", n_particles: int = 0, steps: int = 0, max_depth: int = 0, save_data: bool = False, data_path: str = "", graph_only: bool = False, testing: bool = False, debug: bool = False, print_graph_console: bool = False, refresh_per_second: float = 0):
        self.output_graph_path = output_graph_path
        self.n_particles = n_particles
        self.steps = steps
        self.max_depth = max_depth
        self.save_data = save_data
        self.data_path = data_path
        self.graph_only = graph_only
        self.testing = testing
        self.debug = debug
        self.print_graph_console = print_graph_console
        self.refresh_per_second = refresh_per_second


params:Params = Params()


def setup():
    """
    This method inizialize all params and sets defaults for them if not passed to program
    also set the priority of this process (app) and display to the user current value
    of params useful if execute program without arguments
    """
    app_process = psutil.Process(os.getpid())
    app_process.nice(psutil.HIGH_PRIORITY_CLASS)

    parser = argparse.ArgumentParser(
        description='Neutron Scattering\nRandom walk simulation of neutron scattering',
        epilog='Author: Francesco Vascelli')
    parser.add_argument('-o', '--output', action='store', dest='output', type=str, default=constants.DEFAULT_GRAPH_OUTPUT,
                        help='Output Graph file picture with the result')
    parser.add_argument('-np', '--n_particles', action='store', dest='n_particles', type=int,
                        help='Number of particles', default=constants.DEFAULT_N_PARTICLES)
    parser.add_argument('-s', '--steps', action='store', dest='steps', type=int,
                        help='Number of steps', default=constants.DEFAULT_STEP)
    parser.add_argument('-md', '--max_depth', action='store', dest='max_depth', type=int,
                        help='Number of max depth', default=constants.DEFAULT_MAX_DEPTH)
    parser.add_argument('-sd', '--save_data', action='store_true', dest='save_data',
                        help='Choose if save data in data folder or not', default=constants.DEFAULT_SAVE_DATA)
    parser.add_argument('-dp', '--data_path', action='store', dest='data_path', type=str,
                        help='Location to save data if parameter `--save_data` default ./data', default=constants.DEFAULT_DATA_PATH)
    parser.add_argument('-go', '--graph_only', action='store_true', dest='graph_only',
                        help='Only plot graph width the data provided without execute simulation', default=constants.DEFAULT_GRAPH_ONLY)
    parser.add_argument('-t', '--testing', action='store_true', dest='testing',
                        help='Execute all tests for this program', default=constants.DEFAULT_TESTING)
    parser.add_argument('-dbg', '--debug', action='store_true', dest='debug',
                        help='Execute program in debug mode', default=constants.DEFAULT_DEBUG)
    args = parser.parse_args()

    params.output_graph_path = args.output
    params.n_particles = args.n_particles
    params.steps = args.steps
    params.max_depth = args.max_depth
    params.save_data = args.save_data
    params.data_path = args.data_path
    params.graph_only = args.graph_only
    params.testing = args.testing
    params.debug = args.debug
    params.refresh_per_second = constants.DEFAULT_REFRESH_PER_SECOND

    for arg in sys.argv:
        if not arg.find('-o') > -1:
            params.print_graph_console = True
        else:
            params.print_graph_console = constants.DEFAULT_PRINT_GRAPH_CONSOLE
            break

    if params.testing:
        console_print(message=f"🧪  Execute tests suite: {params.testing}")
    else:
        if not params.print_graph_console:
            console_print(message=f"📈  Output Graph: {params.output_graph_path}")

        console_print(message=f"⚛️  Numbers Of Particles: {params.n_particles}")
        console_print(message=f"🪜  Numbers Of Steps: {params.steps}")
        console_print(message=f"🕳️  Max Depth: {params.max_depth}")

        if params.save_data:
            console_print(message=f"📂  Save Output Data: {params.save_data}")
            console_print(message=f"📂  Data Path Folder: {params.data_path}")

        console_print(message=
            f"📈  Make only graph without simulation: {params.graph_only}")
        console_print(message=f"💻  Output Graph to console {params.print_graph_console}")
        console_print(message=f"🪲  Execute program in debug mode: {params.debug}")

def console_print(message: str, msg_type: str = messageType.MESSAGE_TYPE_NORMAL):
    """
    This method wrap `console.print` method to output message to the user
    """
    if msg_type == messageType.MESSAGE_TYPE_DEBUG:
        debug_sym = "🪲  [DEBUG] "
    else:
        debug_sym = ""
    console.print(f"{debug_sym}{message}")
