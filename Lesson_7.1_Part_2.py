class Vehicle:
    """Base class """
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        """Загальна інформація для транспорту"""
        print(f"Загальна інформація про транспортний засіб: {self.make, self.model, self.year}")


class Car(Vehicle):

    def __init__(self, make, model, year, fuel_type, number_of_doors, number_of_seats):
        super().__init__(make, model, year)
        self.fuel_type = fuel_type
        self.number_of_doors = number_of_doors
        self.number_of_seats = number_of_seats

    def display_info(self):
        """Загальна інформація для машини"""
        print(f"Загальна інформація про транспортний засіб: Це виробник {self.make}, модель {self.model}, з {self.year}, кількість дверей {self.number_of_doors}, кількість місць {self.number_of_seats}")


class Motorcycle(Vehicle):

    def __init__(self, make, model, year, type_of_motorcycle, wheel_count):
        super().__init__(make, model, year)
        self.type_of_motorcycle = type_of_motorcycle
        self.wheel_count = wheel_count

    def display_info(self):
        """Загальна інформація для мотоцикла"""
        print(f"Загальна інформація про транспортний засіб: Це  виробник {self.make}, модель {self.model}, з {self.year}, тип мотоциклу {self.type_of_motorcycle}, має {self.wheel_count} колеса")


class Bicycle(Vehicle):

    def __init__(self, make, model, year, gear_count, has_basket):
         super().__init__(make, model, year)
         self.gear_count = gear_count
         self.has_basket = has_basket

    def display_info(self):
        """Загальна інформація для велосипеда"""
        if self.has_basket is True:
            print(f"Загальна інформація про транспортний засіб: Це: {self.make}, {self.model}, {self.year}, {self.gear_count}, {self.gear_count} gear and  has basket")

        else:
            print(f"Загальна інформація про транспортний засіб: Це: виробник {self.make}  модель {self.model} з {self.year} "
                    f"має {self.gear_count} передачі і немає кошика")



car = Car("Volkswagen", "Touareg", 2008, "disel", 5, 5)
motorcycle = Motorcycle("YAMAHA", "MT", 2024, "sport", 2)
bicycle = Bicycle("Italy", "Crossride Skyline", 2023, 24, False)

list_of_vehicles = [car, motorcycle, bicycle]

for vehicles in list_of_vehicles:
    vehicles.display_info()
