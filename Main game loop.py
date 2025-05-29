#Imports and Global Variables
import pickle
import random
import collections


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