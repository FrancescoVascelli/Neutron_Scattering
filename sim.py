# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 10:28:34 2022

@author: Francesco Vascelli
"""
import time
import init
import utility
import scattering
import testing


def main():
    """
    This method is the entry point for all programs
    """
    t_start = time.perf_counter()
    init.setup()
    params = init.params
    if params.testing:
        testing.test_all_suite() # pylint: disable=no-value-for-parameter
        exit(0)

    if params.graph_only:
        utility.graph_only(data_path=params.data_path,
                          output_graph_path=params.output_graph_path, print_graph_console=params.print_graph_console)
    else:
        parse_data = scattering.scatter(
            n_particles=params.n_particles, steps=params.steps, max_depth=params.max_depth)
        x_depth = parse_data.arr_depth
        n_back = parse_data.arr_back
        n_lost = parse_data.arr_lost
        n_through = parse_data.arr_through

        if params.save_data:
            utility.save_data(data_path=params.data_path, n_back=n_back,
                             n_lost=n_lost, n_through=n_through, x_depth=x_depth)

        utility.graph_plot(n_back=n_back, n_lost=n_lost, n_through=n_through,
                           x_depth=x_depth, output_graph_path=params.output_graph_path, print_graph_console=params.print_graph_console)
        t_end = time.perf_counter()
        utility.execution_time_message(message='Total execution time',time_start=t_start,time_end=t_end)


if __name__ == '__main__':
    main()
