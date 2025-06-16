 ###############################################################################
# Title: Battle Ships
# Name: Graydon
# Class: Computer Science 20
# Assignment: Final Project
# Version: v3
# Date: June 16th 2025
###############################################################################
"""
This program is a multiplayer turn-based naval combat game.

Each player controls a ship fighting on a randomly generated ocean map. On
their turn, they can move the ship and fire shots. Neither player is aware of
the other's exact location. The goal is to sink the other player.
"""
###############################################################################
# Imports and Global Variables-------------------------------------------------
from tabulate import tabulate
import ocean
import vessel
import targetingData
player1Score = 0
player2Score = 0
blanker = """



















"""


# Functions -------------------------------------------------------------------
def player1Turn():
    """Player 1's turn.

    Shows the player the map, then gets their movement.
    Then, lets player fire three times and shows firing locations.
    Finally, sets up for player 2."""
    global blanker
    nextPlayer = input("When player 1 is ready, press Enter.")
    tempMap = oceanMap.map[:]
    tempMap[playerShip1.x][playerShip1.y] = "@"
    print(tabulate(tempMap))
    tempMap[playerShip1.x][playerShip1.y] = " "
    print(f"You hit {int(playerShip2.timesHit)} shots last round.")
    while True:
        validOptions = {"north", "east", "south", "west", "stay"}

        moveDirection = input("Would you like to move NORTH, EAST," +
                              "SOUTH, WEST, or STAY.").lower()
        if moveDirection in validOptions:
            if (moveDirection == "north" and (playerShip1.x - 1) > (-1) and
                oceanMap.map[playerShip1.x - 1][playerShip1.y] == " "
                and not (playerShip1.x - 1 == playerShip2.x
                and playerShip1.y == playerShip2.y)):
                    playerShip1.move(-1, 0)
                    break
            elif (moveDirection == "east" and (playerShip1.y + 1) < 10
                and oceanMap.map[playerShip1.x][playerShip1.y + 1] == " "
                and not (playerShip1.x == playerShip2.x
                and playerShip1.y + 1 == playerShip2.y)):
                    playerShip1.move(0, 1)
                    break
            elif (moveDirection == "south" and (playerShip1.x + 1) < 10
                and oceanMap.map[playerShip1.x + 1][playerShip1.y] == " "
                and not (playerShip1.x + 1 == playerShip2.x
                and playerShip1.y == playerShip2.y)):
                    playerShip1.move(1, 0)
                    break
            elif (moveDirection == "west" and (playerShip1.y - 1) > (-1)
                and oceanMap.map[playerShip1.x][playerShip1.y - 1]== " "
                and not (playerShip1.x == playerShip2.x
                and playerShip1.y - 1 == playerShip2.y)):
                    playerShip1.move(0, -1)
                    break
            elif moveDirection == "stay":
                break
            else:
                print("Invalid movement option. Make sure you aren't " +
                      "trying to crash into a rock or go out of bounds.")

        else:
            print("Invalid input.")
    tempMap = oceanMap.map[:]
    tempMap[playerShip1.x][playerShip1.y] = "@"
    print(tabulate(tempMap))
    tempMap[playerShip1.x][playerShip1.y] = " "
    firing = input("Fire? Type Y or Yes to fire. Anything else will be " +
                   "interpreted as a no.").lower()
    if firing == "y" or firing == "yes":
        print("Please pick three locations to shoot.")
        playerShip1.fire()
        playerShip1.fire()
        playerShip1.fire()
        for target in targetingData.targets:
            tempMap[target[0]][target[1]] = "x"
        print(tabulate(tempMap))
        for target in targetingData.targets:
            tempMap[target[0]][target[1]] = " "
    nextTurn = input("Press Enter, then hand over " +
                     "the computer to the next player")
    print(blanker)
    player2Turn()


def player2Turn():
    """Player 2's turn.

    Shows the player the map, then gets their movement.
    Then, lets player fire three times and shows firing locations.
    Finally, sends things to the turn processor."""
    global blanker
    nextPlayer = input("When player 2 is ready, press Enter.")
    tempMap = oceanMap.map[:]
    tempMap[playerShip2.x][playerShip2.y] = "@"
    print(tabulate(tempMap))
    tempMap[playerShip2.x][playerShip2.y] = " "
    print(f"You hit {int(playerShip1.timesHit)} shots last round.")
    while True:
        tempMap[playerShip2.x][playerShip2.y] = " "
        validOptions = {"north", "east", "south",
                        "west", "stay"}
        moveDirection = input("Would you like to move " +
                              "NORTH, EAST, SOUTH, WEST, " +
                              "or STAY.").lower()
        if moveDirection in validOptions:
            if (moveDirection == "north"
                and (playerShip2.x - 1) > (-1)
                and oceanMap.map[playerShip2.x - 1][playerShip2.y] == " "
                and not (playerShip2.x - 1 == playerShip1.x
                and playerShip2.y == playerShip1.y)):
                    playerShip2.move(-1, 0)
                    break
            elif (moveDirection == "east"
                  and (playerShip2.y + 1) < 10
                  and oceanMap.map[playerShip2.x][playerShip2.y + 1] == " "
                  and not (playerShip2.x == playerShip1.x
                  and playerShip2.y + 1 == playerShip1.y)):
                    playerShip2.move(0, 1)
                    break
            elif (moveDirection == "south"
                  and (playerShip2.x + 1) < 10
                  and oceanMap.map[playerShip2.x + 1][playerShip2.y] == " "
                  and not (playerShip2.x + 1 == playerShip1.x
                           and playerShip2.y == playerShip1.y)):
                    playerShip2.move(1, 0)
                    break
            elif (moveDirection == "west"
                  and (playerShip2.y - 1) > (-1)
                  and oceanMap.map[playerShip2.x][playerShip2.y - 1] == " "
                  and not (playerShip2.x == playerShip1.x
                  and playerShip2.y - 1 == playerShip1.y)):
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
    firing = input("Fire? Type Y or Yes to fire. Anything "
                   + "else will be interpreted as a no.").lower()
    if firing == "y" or firing == "yes":
        print("Please pick three locations to shoot.")
        playerShip2.fire()
        playerShip2.fire()
        playerShip2.fire()
        for target in targetingData.targets:
            tempMap[target[0]][target[1]] = "x"
        print(tabulate(tempMap))
        for target in targetingData.targets:
            tempMap[target[0]][target[1]] = " "
    stall = input("Press Enter to proceed")
    print(blanker)
    turnProcessing()


def turnProcessing():
    """Processes turns and scoring.
    
    Checks the shots of both players, and clears the shot array.
    Checks player health, to see if someone won.
    Finally, sends things back to Player 1."""
    global player1Score
    global player2Score
    playerShip1.checkShots(False)
    playerShip2.checkShots(True)
    targetingData.targets = []
    if playerShip1.health < 1:
        print("Player 2 wins!")
        player2Score = player2Score + 1
        print("Score: Player 1: " + str(player1Score)
              + " Player 2: " + str(player2Score))
        proceed = input("Play Again?")
        player1Turn()
    elif playerShip2.health < 1:
        print("Player 1 wins!")
        player2Score = player2Score + 1
        print("Score: Player 1: " + str(player1Score)
              + " Player 2: " + str(player2Score))
        proceed = input("Play Again?")
        player1Turn()
    player1Turn()


# Main ------------------------------------------------------------------------
oceanMap = ocean.Ocean(10, 10)
oceanMap.map[0][9] = "■"
oceanMap.map[9][0] = "■"
playerShip1 = vessel.Vessel(9, 9, 5)
playerShip2 = vessel.Vessel(0, 0, 5)
print("""The current player is represented by an @ sign. The goal is to find
and destroy the other player's ship. ■ are rocks - they block you, but
are destroyed if shot.""")
      
player1Turn()