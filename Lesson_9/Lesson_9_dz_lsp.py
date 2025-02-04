import math
from abc import ABC,  abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def print(self):
        pass

    def __str__(self):
        return self.__class__.__name__.lower()


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def print(self):
        return "Shape №1"

    def area(self):
        return math.pi * (self.r ** 2)

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def print(self):
        return "Shape №2"

    def area(self):
        return  self.side ** 2

def print_area(shape: Shape):
        print(f"{shape.print()}\nArea of shape {shape} is {shape.area()}")


circle = Circle(3)
square = Square(4)


print_area(circle)
print_area(square)
