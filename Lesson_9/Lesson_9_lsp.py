


class Car:
    def __init__(self, type):
        self.type = type
        self.properties = {}

    def set_properties(self, color, cost, capacity):
        self.properties = {"Color": color, "Cost": cost, "Capacity": capacity}

    def get_properties(self):
        return self.properties


class Car2(Car):
    pass
    # def __init__(self, type):
    #     super().__init__(type)


class Car3(Car):
    pass
    # def __init__(self, type):
    #     super().__init__(type)


car = Car("Toyota")
car.set_properties("Red", 10000, 6)

car2 = Car2("Volvo")
car2.set_properties("Blue", 5000, 4)

car3 = Car3("Mersedess")
car3.set_properties("Grin", 6000, 8)

cars = [car, car2, car3]

def get_concrete_color_car(color):
    count = 0
    car_types = []
    for car in cars:
        if car.properties["Color"] == color:
            count +=1
            car_types.append(car.type)
    print(f"Count of {color} cars: {count}\nCar types: {car_types}" )


def get_concrete_cost_car(cost):
    count = 0
    car_types = []
    for car in cars:
        if car.properties["Cost"] == cost:
            count +=1
            car_types.append(car.type)
    print(f"Count of {cost} cars: {count}\nCar types: {car_types}")


get_concrete_color_car("Grin")
get_concrete_cost_car(5000)


for car_all in cars:
    print(f"Type: {car_all.type}, Properties: {car_all.get_properties()}")