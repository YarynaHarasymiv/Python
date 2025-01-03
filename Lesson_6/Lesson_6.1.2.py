class Rectangle:
    """Створення класу `Rectangle"""
    def __init__(self, width, height):
        """Ініціалізація атрибутів"""
        self.width = width
        self.height = height

    def calculate_area(self):
        """Метод для обчислення площі прямокутника"""
        return self.height * self.height

area1 = Rectangle(2, 4)
area2 = Rectangle(5, 6)

print(f"Площа першого прямокутника : {area1.calculate_area()}")
print(f"Площа другого прямокутника : {area2.calculate_area()}")