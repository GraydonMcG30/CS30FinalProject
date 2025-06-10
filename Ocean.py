import random
class Ocean:
    def __init__ (self, height, width):
        self.width = width
        self.height = height
        self.map = self.makeMap()
    def makeMap(self):
        map_ = []
        for row in range(self.height):
            map_.append([])
            for column in range(self.width):
                if random.randint(1, 5) > 4:
                    map_[row].append("■")#blocker
                else:
                    map_[row].append(" ")
        map_[0][0] = []
        map_[9][9] = []
        return map_

                
        
        
        