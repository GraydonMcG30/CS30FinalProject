#Imports and Global Variables
import targetingData

#Classes
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
        self.exists = True
        
    def takeDamage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.exists = False
        
    def move(self, xshift, yshift):
        self.x = x + xshift
        self.y = y + yshift
    
    def fire(self):
        while True:
            coord1 = int(input("Please input the target column."+
                                      "Must be within 5 tiles.")) - 1
            coord2 = int(input("Please input the target row."+
                                      "Must be within 5 tiles.")) - 1
            if coord1 > self.x - 6 and coord1 < self.x + 6 and coord2 > self.y - 6 and coord2 < self.y + 6:
                newTuple = (coord1, coord2)
                targetingData.targets.append(newTuple)
                break
            else:
                print("Out of range.")
            
    def checkShots(self):
        for target in targetingData.targets:
            if self.x == target[0] and self.y == target[1]:
                print("Test")
        

    