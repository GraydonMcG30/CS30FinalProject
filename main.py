#Imports and Global Variables
from tabulate import tabulate
import ocean
import vessel



#Functions


#Main
#This will be replaced with proper initializing code later.
oceanMap = ocean.Ocean(10, 10)
playerShip1 = vessel.Vessel(9, 9, 5)
playerShip2 = vessel.Vessel(0, 0, 5)

def player1Turn():
    print("Please pick three locations to shoot.")
    playerShip1.fire()
    playerShip1.fire()
    playerShip1.fire()
    while True:
        validOptions = {"north", "east", "south", "west", "stay"}
        moveDirection = input("Would you like to move NORTH, EAST, SOUTH, WEST, or STAY.").lower()
        if moveDirection in validOptions:
            if moveDirection == "north" and oceanMap.map[playerShip1.x][playerShip1.y - 1] == " " and (playerShip1.y - 1) > (-1):
                playerShip1.move(0,-1)
            elif moveDirection == "east" and oceanMap.map[playerShip1.x + 1][playerShip1.y] == " " and (playerShip1.x + 1) < 10:
                playerShip1.move(1, 0)
            if moveDirection == "south" and oceanMap.map[playerShip1.x][playerShip1.y - 1] == " " and (playerShip1.y + 1) < 10:
                playerShip1.move(0,1)
            elif moveDirection == "west" and oceanMap.map[playerShip1.x - 1][playerShip1.y] == " " and (playerShip1.x - 1) > (-1):
                playerShip1.move(-1, 0)
            else:
                break
        else:
            print("Invalid movement option. Make sure you aren't trying to crash into a rock.")



player1Turn()
tempMap = oceanMap.map.copy()
tempMap[playerShip1.x][playerShip1.y] = "@"
print(tabulate(tempMap))
playerShip1.checkShots()