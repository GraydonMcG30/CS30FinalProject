#Imports and Global Variables
from tabulate import tabulate
import ocean
import vessel



#Functions


#Main
#This will be replaced with proper initializing code later.
oceanMap = ocean.Ocean(10, 10)
playerShip = vessel.Vessel(9, 9, 5)
enemyShip = vessel.Vessel(0, 0, 5)

def playerTurn():
    print("Please pick three locations to shoot.")
    playerShip.fire()
    playerShip.fire()
    playerShip.fire()

    while True:
        movementDirection = input("Would you like to move NORTH, EAST, SOUTH, WEST, or STAY.").lower
        if movementDirection == "north":
            playerShip.move(0, 1)
            break
        elif movementDirection == "south":
            playerShip.move(0, -1)
            break
        elif movementDirection == "east":
            playerShip.move(1, 0)
            break
        elif movementDirection == "west":
            playerShip.move(-1, 0)
            break
        elif movementDirection == "stay":
            break
        else:
            pass
        break

        
playerTurn()
playerShip.checkShots()
            