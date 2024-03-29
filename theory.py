import sys

from sympy import factor
sys.dont_write_bytecode = True
import scipy.constants as const
import numpy as np
from Simulation import Simulation

sim = Simulation()

dt = sim.dt
N = sim.N
T = sim.T
m = sim.particles[0].mass
FP = sim.meanFP
nd = sim.nd
r = sim.particles[0].radius
FN = sim.FN
volume = sim.volume

 
def rmsSpeed():
    """Calculate the root-mean-square speed of particles

    Args:

        :return: Root-mean-square particle speed (m/s)
    """
    rmsSpeed = np.sqrt((2 * const.k * T)/m)
    print('rmsSpeed: ' + str(rmsSpeed))
    return rmsSpeed


def mostProbableSpeed():
    """Calculate the most probable particle speed

    Args:

        :return: Most probable particle speed (m/s)
    """
    probSpeed = np.sqrt((const.k * T)/m)
    print('probSpeed: ' + str(probSpeed))
    return probSpeed


def meanSpeed():
    """Calculate the mean particle speed

    Args:

        :return: Mean particle speed (m/s)
    """
    meanSpeed = np.sqrt((const.k * T * const.pi)/(2 * m))
    print('meanSpeed: ' + str(meanSpeed))
    return meanSpeed


def averageCollisionFrequency():
    """Calculate the average collision frequency of 1 particle

    Args:

        :return: The average number of collisions in a system per second per unit volume
    """
    Z = meanSpeed()/FP
    # print('collision frequency: ' + str(Z))
    return Z


def totalCollisionNumber():
    """Calculate the average total number of collisions per unit volume and time

    Args:

        :return: The average number of collisions in a system per second per meter squared
    """
    colNum = averageCollisionFrequency() * 1/2 * nd
    # print('Total coll: ' + str(colNum))
    return colNum


def totalEnergy():
        """Calculate the total energy of the system from the mean speed value

	    Args:

		    :return: Total energy of the system [J]
	    """
        E = 1/2 * m * FN * meanSpeed()**2
        print('E: ' + str(E))
        return E


# totalEnergy()




print('totalCollisionNumber: ' + str(totalCollisionNumber() * dt * volume / FN))

# mostProbableSpeed()
# meanSpeed()
# rmsSpeed()


# # to choose initial maxRS
# print(meanSpeed() * np.sqrt(2) * 2)


for i in range(100):
    sim.advance()

tot = 0
for i in sim.collisions:
    tot += i
print(tot/len(sim.collisions))

# sim.advance()