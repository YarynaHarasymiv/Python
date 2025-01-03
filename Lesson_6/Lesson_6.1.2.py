class Rectangle:
    """Створення класу `Rectangle"""
    def __init__(self, width, height):
        """Ініціалізація атрибутів"""
        self.width = width
        self.height = height

    def calculate_area(self):
        """Метод для обчислення площі прямокутника"""
        return self.height * self.height

Rectangle1 = Rectangle(2, 4)
Rectangle2 = Rectangle(5, 6)

print(f"Площа першого прямокутника : {Rectangle1.calculate_area()}")
print(f"Площа другого прямокутника : {Rectangle2.calculate_area()}")