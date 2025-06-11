#Imports and Global Variables
from tabulate import tabulate
import ocean
import vessel
import targetingData
player1Score = 0
player2Score = 0


#Functions


#Main
#This will be replaced with proper initializing code later.
oceanMap = ocean.Ocean(10, 10)
oceanMap.map[0][9] = "■"
oceanMap.map[9][0] = "■"
playerShip1 = vessel.Vessel(9, 9, 5)
playerShip2 = vessel.Vessel(0, 0, 5)

def player1Turn():
    tempMap = oceanMap.map[:]
    tempMap[playerShip1.x][playerShip1.y] = "@"
    print(tabulate(tempMap))
    tempMap[playerShip1.x][playerShip1.y] = " "
    while True:
        validOptions = {"north", "east", "south", "west", "stay"}

        moveDirection = input("Would you like to move NORTH, EAST, SOUTH, WEST, or STAY.").lower()
        if moveDirection in validOptions:
            if moveDirection == "north" and (playerShip1.x - 1) > (-1) and oceanMap.map[playerShip1.x - 1][playerShip1.y] == " ":
                playerShip1.move(-1, 0)
                break
            elif moveDirection == "east"  and (playerShip1.y + 1) < 10 and oceanMap.map[playerShip1.x][playerShip1.y + 1] == " ":
                playerShip1.move(0, 1)
                break
            elif moveDirection == "south" and (playerShip1.x + 1) < 10 and oceanMap.map[playerShip1.x + 1][playerShip1.y] == " " :
                playerShip1.move(1, 0)
                break
            elif moveDirection == "west" and (playerShip1.y - 1) > (-1) and oceanMap.map[playerShip1.x] [playerShip1.y - 1]== " ":
                playerShip1.move(0, -1)
                break
            elif moveDirection == "stay":
                break
            else:
                print("Invalid movement option. Make sure you aren't trying to crash into a rock or go out of bounds.")

        else:
            print("Invalid input.")
    tempMap = oceanMap.map[:]
    tempMap[playerShip1.x][playerShip1.y] = "@"
    print(tabulate(tempMap))
    tempMap[playerShip1.x][playerShip1.y] = " "
    firing = input("Fire? Type Y or Yes to fire. Anything else will be interpreted as a no.").lower()
    if firing == "y" or firing == "yes":
        print("Please pick three locations to shoot.")
        playerShip1.fire()
        playerShip1.fire()
        playerShip1.fire()
        for target in targetingData.targets:
            tempMap[target[0]][target[1]] = "x"
        print(tabulate(tempMap))
        stall = input("Proceed.")
        for target in targetingData.targets:
            tempMap[target[0]][target[1]] = " "
    print("""
















    """)
    player2Turn()


def player2Turn():
    tempMap = oceanMap.map[:]
    tempMap[playerShip2.x][playerShip2.y] = "@"
    print(tabulate(tempMap))
    tempMap[playerShip2.x][playerShip2.y] = " "
    while True:
        tempMap[playerShip2.x][playerShip2.y] = " "
        validOptions = {"north", "east", "south", "west", "stay"}
        moveDirection = input("Would you like to move NORTH, EAST, SOUTH, WEST, or STAY.").lower()
        if moveDirection in validOptions:
            if moveDirection == "north" and (playerShip2.x - 1) > (-1) and oceanMap.map[playerShip2.x - 1][playerShip2.y] == " ":
                playerShip2.move(-1, 0)
                break
            elif moveDirection == "east"  and (playerShip2.y + 1) < 10 and oceanMap.map[playerShip2.x][playerShip2.y + 1] == " ":
                playerShip2.move(0, 1)
                break
            elif moveDirection == "south" and (playerShip2.x + 1) < 10 and oceanMap.map[playerShip2.x + 1][playerShip2.y] == " " :
                playerShip2.move(1, 0)
                break
            elif moveDirection == "west" and (playerShip2.y - 1) > (-1) and oceanMap.map[playerShip2.x] [playerShip2.y - 1]== " ":
                playerShip2.move(0, -1)
                break
            elif moveDirection == "stay":
                break
            else:
                print("Invalid movement option. Make sure you aren't trying to crash into a rock or go out of bounds.")

        else:
            print("Invalid input.")
    tempMap = oceanMap.map[:]
    tempMap[playerShip2.x][playerShip2.y] = "@"
    print(tabulate(tempMap))
    tempMap[playerShip2.x][playerShip2.y] = " "
    firing = input("Fire? Type Y or Yes to fire. Anything else will be interpreted as a no.").lower()
    if firing == "y" or firing == "yes":
        print("Please pick three locations to shoot.")
        playerShip2.fire()
        playerShip2.fire()
        playerShip2.fire()
        for target in targetingData.targets:
            tempMap[target[0]][target[1]] = "x"
        print(tabulate(tempMap))
        stall = input("Proceed.")
        for target in targetingData.targets:
            tempMap[target[0]][target[1]] = " "
        print("""
















    """)
    turnProcessing()
    


def turnProcessing():
    global player1Score
    global player2Score
    playerShip1.checkShots()
    playerShip2.checkShots()
    targetingData.targets = []
    if playerShip1.health < 1:
        print("Player 2 wins!")
        player2Score = player2Score + 1
        print("Score: Player 1: " + str(player1Score) + " Player 2: " + str(player2Score))
        print("Play Again?")
        player1Turn()
    elif playerShip2.health < 1:
        print("Player 1 wins!")
        player2Score = player2Score + 1
        print("Score: Player 1: " + str(player1Score) + " Player 2: " + str(player2Score))
        print("Play Again?")
        player1Turn()
    print("""
















    """)
    player1Turn()
        
        
player1Turn()

