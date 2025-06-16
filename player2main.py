#Imports and Global Variables
from tabulate import tabulate
import ocean
import vessel
import pickle
import targetingData
player1Score = 0
player2Score = 0
blanker = """



















"""


#Functions


#Main
#This will be replaced with proper initializing code later.
oceanMap = ocean.Ocean(10, 10)
oceanMap.map[0][9] = "■"
oceanMap.map[9][0] = "■"
playerShip1 = vessel.Vessel(9, 9, 5)
playerShip2 = vessel.Vessel(0, 0, 5)

def player2Turn():
    global blanker
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
            elif moveDirection == "south" and (playerShip2.x + 1) < 10 and oceanMap.map[playerShip2.x + 1][playerShip2.y] == " ":
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
        playerShip2.fire(2)
        playerShip2.fire(2)
        playerShip2.fire(2)
        for target in targetingData.ship2targets:
            tempMap[target[0]][target[1]] = "x"
        print(tabulate(tempMap))
        for target in targetingData.ship2targets:
            tempMap[target[0]][target[1]] = " "
    pickleSave()
    nextTurn = input("Press Enter to proceed when you have received the other player's turn.")
    pickleLoad()
    turnProcessing()
    

def pickleSave():
    dataToPickle = {}
    dataToPickle["P2Health"] = playerShip2.health
    dataToPickle["P2X"] = playerShip2.x
    dataToPickle["P2Y"] = playerShip2.y
    dataToPickle["P2targets"] = targetingData.ship2targets
    pickle.dump(dataToPickle, open("p2turn.txt", "wb"))
    

def pickleLoad():
    loadedData = pickle.load(open("p1turn.txt", "rb"))
    playerShip1.health = loadedData["P1Health"]
    playerShip1.x = loadedData["P1X"]
    playerShip1.y = loadedData["P1Y"]
    targetingData.ship2targets = loadedData["P1targets"]


def turnProcessing():
    global player1Score
    global player2Score
    playerShip1.checkShots(1)
    playerShip2.checkShots(True)
    targetingData.targets = []
    if playerShip1.health < 1:
        print("Player 2 wins!")
        player2Score = player2Score + 1
        print("Score: Player 1: " + str(player1Score) + " Player 2: " + str(player2Score))
        proceed = input("Play Again?")
        player2Turn()
    elif playerShip2.health < 1:
        print("Player 1 wins!")
        player2Score = player2Score + 1
        print("Score: Player 1: " + str(player1Score) + " Player 2: " + str(player2Score))
        proceed = input("Play Again?")
        player2Turn()
    player2Turn()
        
        
player2Turn()


