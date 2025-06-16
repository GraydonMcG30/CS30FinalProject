# Imports and Global Variables-------------------------------------------------
import random


# Classes ---------------------------------------------------------------------
class Ocean:
    """An ocean map."""
    
    def __init__(self, height, width):
        """Parameters:
        width: map width, int.
        height: map height, int."""
        
        self.width = width
        self.height = height
        self.map = self.makeMap()

    def makeMap(self):
        """Makes a map.
        
        Creates a map array, adds random blockers,
        and clears the corners for vessels."""
        map_ = []
        for row in range(self.height):
            map_.append([])
            for column in range(self.width):
                if random.randint(1, 5) > 4:
                    map_[row].append("■")  # blocker
                else:
                    map_[row].append(" ")
        map_[0][0] = " "
        map_[9][9] = " "
        return map_