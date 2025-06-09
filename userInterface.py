#Imports and Global Variables
from tabulate import tabulate
import ocean
import vessel
import turnProcessor



#Functions


#Main
oceanMap = ocean.Ocean(10, 10)
playerShip = vessel.Vessel(9, 9, 10)
enemyShip = vessel.Vessel(0, 0, 10)
playerShip.fire()
print(turnProcessor.targets)