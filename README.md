# Neutron Scattering
 
 stuff
 
## Random walk simulation of neutron scattering

The following code simulates the scattering of multiple neutrons inside a reactor wall using a 2D random walk. The main steps are:

1. The neutron initial velocity is perpendicular to the wall.
2. The only possible directions of motion are left, right, up and down.
3. At each step the neutron can not step back, but only forward, left or right.
4. The probability to go forward is double than changing direction.
5. After each step, the position of the neutron is checked:
    - if it is back inside the reactor or outside the wall, register its position and go to the next neutron.
    - otherwise, continue with another step.
6. After a set amount of steps (100 by default), the neutron stops.

Repeat all steps for a set amount of neutrons (5,000 by default).

Calculate the probabilities for neutrons (as a function of the wall depth):
- to be back in the reactor
- to be captured in the reactor wall
- to get through the reactor wall
 
![](http://ww2.odu.edu/~agodunov/teaching/phys420/files/reactor.gif)


Note: 
Each step is considered as the mean free path between interactions. 
In the same way, the reactor wall depth is expressed in units of steps.


## How to run the simulation

In order to run the code and plot the results, the user must:
1. Install all the necessary libraries using the preferred installer (like `pip` or `conda`). 
The libraries used in this code are numpy, configparser, tqdm, time, os, sys, matplotlib and hypothesis.
2. Launch the file [sim.py](/sim.py) which imports its parameters from [settings.txt](/settings.txt) using configparser library. 
To do so, write `python sim.py settings.txt` in the command line. This can take a few minutes. 
If the user wishes to, they can modify the input parameters (n_particles and steps) in the settings.txt file or create a new one with the same syntax and call it instead of settings.txt.
The resulting data are saved in the **data** folder using their local paths.
3. At the end, launch the file [plot.py](/plot.py) with the same configuration. 
To do so, type `python plot.py settings.txt` in the command line. The data are loaded from settings.txt through their local paths and the resulting plot is saved in the **images** folder. 
 
## Project structure

The code is separated in different files:
- In [scattering.py](/scattering.py) there are all the custom functions necessary for the 2D random walk.
 After the neutron ends its walk, the function saves its final position in an array for data analysis.
- In [testing.py](/testing.py) there are a few tests for all the functions of the random walk, with hypothesis testing.
- In [settings.txt](/settings.txt) there are the input values taken by the simulation file (number of initial neutrons and steps before stopping).
In addition, there are the local paths to load the array data and to save the final plot.
- In [sim.py](/sim.py) there is the main part of the code. The random walk is performed for each neutron and the data resulting from the scattering file are used to calculate
the probability of each final state. Furthermode, this calculation is done for different depths of the reactor wall in a defined range and the results are all saved for plotting.
- In [plot.py](/plot.py) there is a function that plots the probability of the final states as a function of the depth, loading the data from the saved arrays using configparser.

To give an example result, below there is a plot of the probability as a function of depth, using the default configuration.

![](/images/ratio.png)


