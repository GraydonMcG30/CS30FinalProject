


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
        
    def move(xshift, yshift):
        self.x = x + xshift
        self.y = y + yshift
    

    