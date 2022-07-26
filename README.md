# Neutron Scattering
 
 stuff
 
## Random walk simulation of neutron scattering

The following code simulates the scattering of multiple neutrons inside a reactor wall using a 2D random walk. The main steps are:

1. The neutron initial velocity is perpendicular to the wall.
2. The only possible directions of motion are left, right, up and down.
3. At each step the neutron can not step back, but only forward, left or right.
4. The probability to go forward is double than changing direction.
5. After each step, the position of the neutron is checked:
    - if it's back inside the reactor or outside the wall, register its position and go to the next neutron.
    - otherwise, continue with another step.
6. After a set amount of steps (100 by default), the neutron stops.

Repeat all steps for a set amount of neutrons (10,000 by default).

Calculate the probabilities for neutrons (as a function of the wall depth):
- to be back in the reactor
- to be captured in the reactor wall
- to get through the reactor wall

Note: each step is considered as the mean free path between interactions. In the same way, the reactor wall depth is expressed in units of steps.
![](http://ww2.odu.edu/~agodunov/teaching/phys420/files/reactor.gif)
## How to run the simulation

In order to run the code and plot the results, the user must:
1. Install all the necessary libraries 
