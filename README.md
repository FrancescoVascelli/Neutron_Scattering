# Neutron Scattering

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
1. Install all the necessary libraries using the command `python -m pip install -r requirements.txt`

The libraries used in this code are the standard one (cames with python) + module in the `requirements.txt`

2. Launch the file [sim.py](/sim.py), if the user don't provide any arguments the simulation takes the default value quoted above and the plot output directly in the terminal.
    - In order to know what arguments available for this program run this command: `python sim.py --help`
    - By default this program **don't** save `.npy` files but you can providing `--save_data` param to the program in this case the resulting data are saved in the **data** folder inside current directory or the folder you specify folder.
3. By default the program output the result plot directly in the terminal window but if you specify `--output=FOLDER_PATH` the output is saved in the directory you specify
 
## Project structure

The code is separated in different files:
- In [scattering.py](/scattering.py) there are all the custom functions necessary for the 2D random walk.
 After the neutron ends its walk, the function saves its final position in an array for data analysis.
- In [testing.py](/testing.py) there are a few tests for all the functions of the random walk, with hypothesis testing.
- In [sim.py](/sim.py) there is the main part of the code. The random walk is performed for each neutron and the data resulting from the scattering file are used to calculate
the probability of each final state. Furthermode, this calculation is done for different depths of the reactor wall in a defined range and the results are all saved for plotting.


To give an example result, below there is a plot of the probability as a function of depth, using the default configuration.

![](/images/ratio.png)


