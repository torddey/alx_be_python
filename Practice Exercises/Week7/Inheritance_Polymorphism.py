# Exercise 1: Single Inheritance Instruction:
# •	Create a base class Shape with a method calculate_area().
# •	Create a subclass Rectangle that inherits from Shape and overrides calculate_area() to calculate the area of a rectangle.
# Exercise 2: Multiple Inheritance Instruction:
# •	Create two parent classes Bird and Mammal with methods fly() and run(), respectively.
# •	Create a subclass Bat that inherits from both Bird and Mammal and implements fly() and run() methods
# Exercise 3: Polymorphism with Duck Typing Instruction:
# •	Create classes Dog, Cat, and Bird, each with a method make_sound().
# •	Implement different behaviors for make_sound() in each class.
# •	Create a function let_them_speak() that takes a list of objects and calls their make_sound() method polymorphically.

class Shape:
    def __init__(self, name):
        self.name = name
       

    def calculate_area(self, lenght, width):
        self.lenght = lenght
        self.width = width
        return f"{self.lenght} * {self.width}"
        

class Rectangle (Shape):
    pass