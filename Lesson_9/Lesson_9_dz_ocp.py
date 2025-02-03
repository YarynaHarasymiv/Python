import math
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class ShapeCircle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return f"Площа кола, де r = {self.r} : {math.pi * self.r ** 2}"


class ShapeRectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return f"Площа прямокутника, де width = {self.width}, height = {self.height}: {self.height * self.width}"


def print_area(shape: Shape):
    print(f"{shape.area()}")

shape_rectangle = ShapeRectangle(3, 4)
shape_circle = ShapeCircle(3)

print_area(shape_rectangle)
print_area(shape_circle)





