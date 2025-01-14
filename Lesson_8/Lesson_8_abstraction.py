from abc import ABC, abstractclassmethod, abstractmethod


class Car(ABC):

    def __init__(self, mark, cost):
        self.mark = mark
        self.cost =cost

    @classmethod
    @abstractmethod
    def car_preview(cls):
        pass

class Toyota(Car):

    def car_preview(self):
        print(f"Car {self.mark} costs {self.cost}")

class Mersedes(Car):
    def car_preview(self):
        print(f"Car {self.mark} costs {self.cost}")


class BMW(Car):
    pass

# toyota = Toyota("off_road", 1000)
# toyota.car_preview()
# mersedes = Mersedes("crossover", 5000)
# mersedes.car_preview()
# bmw = BMW("city+type", 4000)
# bmw.car_preview()



class Animal(ABC):

    @classmethod
    @abstractmethod
    def move(cls):
        pass

    @classmethod
    @abstractmethod
    def eat(cls):
        pass

class Cat(Animal):

    def __init__(self, color, age):
        self.color = color
        self.age = age

    def move(self):
        print(f"Cat has {self.color} color moves to ahead")

    def eat(self):
        print(f"Cat ate this food {self.age} years")


class Dog(Animal):

    def __init__(self, distance, food_type):
        self.distance = distance
        self.food_type = food_type

    def move(self):
        print(f"Dog walked {self.distance} km")

    def eat(self):
        print(f"Dog ate this {self.food_type} today")

class AnimalType(Animal):
    pass

class Bird(AnimalType):

    def __init__(self, name):
        self.name = name

    def move(self):
        print(f"Bird {self.name} flies")

    def eat(self):
        print(f"Bird {self.name} ate two days ago")


cat = Cat("red", 7)
cat.move()
cat.eat()

dog = Dog(10, "meat")
dog.move()
dog.eat()

bird = Bird("Lusy")
bird.move()
bird.eat()

animal_type = AnimalType()
animal_type.move()
animal_type.eat()