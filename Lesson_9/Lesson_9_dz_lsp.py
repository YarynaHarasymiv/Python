import math
from abc import ABC,  abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    def print_area(self):
        pass

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return math.pi * (self.r ** 2)

    def __str__(self):
        return f"circle"

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return  self.side ** 2

    def __str__(self):
        return f"square"

def print_area(shape: Shape):
        print(f"Area of shape {shape} is {shape.area()}")


circle = Circle(3)
square = Square(4)

print_area(square)
print_area(circle)
