class Rectangle:
    def __init__(self, x=0, y=0, width=0, height=0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __str__(self):
        return (f"{self.__class__.__name__} ({self.x}, {self.y}, {self.width}, {self.height})")

s1 = Rectangle(x=7, y=11, width=999, height=1000)
print(s1)