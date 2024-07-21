import math

class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, lenght = int, width= int):
        self.lenght = lenght 
        self.width = width

    def area(self):
        return self.lenght * self.width

class Circle(Shape):
    def __init__(self, radius= int):
       self.radius = radius
       
    def area(self):
        return math.pi * (self.radius ** 2)


