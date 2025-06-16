#Imports and Global Variables
from tabulate import tabulate
import pickle
import ocean
import vessel
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

def player1Turn():
    global blanker
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
            elif moveDirection == "south" and (playerShip1.x + 1) < 10 and oceanMap.map[playerShip1.x + 1][playerShip1.y] == " ":
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
        playerShip1.fire(1)
        playerShip1.fire(1)
        playerShip1.fire(1)
        for target in targetingData.ship1targets:
            tempMap[target[0]][target[1]] = "x"
        print(tabulate(tempMap))
        for target in targetingData.ship1targets:
            tempMap[target[0]][target[1]] = " "
    pickleSave()
    nextTurn = input("Press Enter to proceed when you have received the other player's turn.")
    pickleLoad()
    turnProcessing()



def pickleSave():
    dataToPickle = {}
    dataToPickle["P1Health"] = playerShip1.health
    dataToPickle["P1X"] = playerShip1.x
    dataToPickle["P1Y"] = playerShip1.y
    dataToPickle["P1targets"] = targetingData.ship1targets
    pickle.dump(dataToPickle, open("p1turn.txt", "wb"))
    print("Save complete. Please send your turn to the other player.")
    

def pickleLoad():
    loadedData = pickle.load(open("p2turn.txt", "rb"))
    playerShip2.health = loadedData["P2Health"]
    playerShip2.x = loadedData["P2X"]
    playerShip2.y = loadedData["P2Y"]
    targetingData.ship2targets = loadedData["P2targets"]


def turnProcessing():
    global player1Score
    global player2Score
    playerShip1.checkShots(1)
    playerShip2.checkShots(2)
    targetingData.targets = []
    if playerShip1.health < 1:
        print("Player 2 wins!")
        player2Score = player2Score + 1
        print("Score: Player 1: " + str(player1Score) + " Player 2: " + str(player2Score))
        proceed = input("Play Again?")
        player1Turn()
    elif playerShip2.health < 1:
        print("Player 1 wins!")
        player2Score = player2Score + 1
        print("Score: Player 1: " + str(player1Score) + " Player 2: " + str(player2Score))
        proceed = input("Play Again?")
        player1Turn()
    player1Turn()
        


player1Turn()


