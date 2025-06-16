# Imports and Global Variables-------------------------------------------------
import targetingData


# Classes ---------------------------------------------------------------------
class Vessel:
    """Any and all ships."""

    def __init__(self, x, y, health):
        """Parameters:
           x: X coordinate of ship - integer
           y: Y coordinate of ship - integer
           health: Health of ship - integer
        """
        self.x = x
        self.y = y
        self.health = health
        self.timesHit = 0
        
    def move(self, xshift, yshift):
        """Moves the vessel by the inputed shift values."""
        self.x = self.x + xshift
        self.y = self.y + yshift
    
    def fire(self):
        """Fire shots.
        Loops to take user input, and checks input is in range.
        Then, appends the input coordinates as tuples to targetingData
        """
        while True:
            try:
                coord1 = int(input("Please input the target row."+
                                      "Must be within 5 tiles.")) - 1
                coord2 = int(input("Please input the target column."+
                                      "Must be within 5 tiles.")) - 1
                if (coord1 > self.x - 6 and coord1 < self.x + 6
                    and coord2 > self.y - 6 and coord2 < self.y + 6
                    and coord1 > 0 and coord2 > 0):
                        newTuple = (coord1, coord2)
                        targetingData.targets.append(newTuple)
                        break
                else:
                    print("Out of range.")
            except ValueError:
                print("Please input an integer.")
            
    def checkShots(self, destroy):
        """Checks fired shots.

        Parameters:
        destroy: Should the array of shots be cleared - bool
        
        Checks targetingData for overlapping shots, then
        damages the vessel. Records amount of shots hit,
        then clears shot array after checking p2."""
        self.timesHit = 0
        for target in targetingData.targets:
            if self.x == target[0] and self.y == target[1]:
                print( "Player Hit")
                self.health = self.health - 1
                self.timesHit = self.timesHit +  1
        if destroy:
            targetingData.targets = []