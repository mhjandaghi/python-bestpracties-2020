class Coordinates:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def info(self): # __str__
        print(f"x: {self.x}\ny: {self.y}")

    def distance(self, other):
        c = (((other.x - self.x) ** 2) + ((other.y - self.y) ** 2) )** 0.5
        return c
    
    def slope(self, other):
        print((self.y - other.y) / (self.x - other.x))

