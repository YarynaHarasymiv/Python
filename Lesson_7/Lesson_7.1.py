
class Vehicle:
    """Base class """
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year


class Car(Vehicle):
    def __init__(self, make, model, year, fuel_type, number_of_doors, number_of_seats):
        super().__init__(make, model, year)
        self.fuel_type = fuel_type
        self.number_of_doors = number_of_doors
        self.number_of_seats = number_of_seats

    def start_engine_1(self):
        print(f"Car {self.make} {self.model} since {self.year} "
              f"has {self.number_of_doors} doors "
              f"and {self.number_of_seats} seats in the car")



class Motorcycle(Vehicle):
    def __init__(self, make, model, year, type_of_motorcycle, wheel_count):
        super().__init__(make, model, year)
        self.type_of_motorcycle = type_of_motorcycle
        self.wheel_count = wheel_count

    def start_engine_2(self):
        print(f"Motorcycle {self.make} {self.model} since {self.year}"
              f" has {self.type_of_motorcycle} type and {self.wheel_count} wheel")



class Bicycle(Vehicle):
    def __init__(self, make, model, year, gear_count, has_basket):
        super().__init__(make, model, year)
        self.gear_count = gear_count
        self.has_basket = has_basket

    def start_engine_3(self):
        if self.has_basket is True:
            print(f"Bicycle from {self.make} {self.model} since {self.year} "
              f"has {self.gear_count} gear and  has basket")

        else:
            print(f"Bicycle from {self.make} {self.model} since {self.year} "
              f"has {self.gear_count} gear and dont have basket")


car_value = Car("Volkswagen", "Touareg", 2008, "disel", 5, 5)
Motorcycle_value = Motorcycle("YAMAHA", "MT", 2024, "sport", 2)
Bicycle_value = Bicycle("Italy", "Crossride Skyline", 2023, 24, False)

car_value.start_engine_1()
Motorcycle_value.start_engine_2()
Bicycle_value.start_engine_3()