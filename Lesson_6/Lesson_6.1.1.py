class Animal:
    """Клас для представлення тварини"""
    def __init__(self, name, species, age):
        """Ініціалізація атрибутів класу."""
        self.name = name
        self.species = species
        self.age = age

    def make_sound(self):
        """Виводить звук, який виділяє тварина."""
        print(f"{self.name} виводить звук який виділяє тварина {self.species}")


animal1 = Animal("Vine", "cat", 3)
animal2 = Animal("Leila", "dog", 4)


animal1.make_sound()
animal2.make_sound()
