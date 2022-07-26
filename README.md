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

Repeat all steps for a set amount of neutrons (10,000 by default).

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
1. Install all the necessary libraries using the preferred installer (like 'pip' or 'conda'). 
The libraries used in this code are numpy, configparser, tqdm, time, os, sys, matplotlib and hypothesis.
2. Launch the file [sim](/sim.py) which imports its parameters from [settings](/settings.txt) using configparser library. 
To do so, write 'python sim.py settings.txt' in the command line. This can take a few minutes. 
If the user wishes to, they can modify the input parameters (n_particles and steps) in the settings.txt file or create a new one with the same syntax and call it instead of settings.txt.
The resulting data are saved in the **data** folder using their local paths.
3. At the end, launch the file [plot](/plot.py) with the same configuration. 
To do so, type 'python plot.py settings.txt' in the command line. The data are loaded from settings.txt through their local paths and the resulting plot is saved in the **images** folder. 
 
## Project structure

