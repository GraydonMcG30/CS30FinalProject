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
                map_[row].append([])
        return map_
    
oceanMap = Ocean(10, 10)
print(oceanMap.map)
                
        
        
        