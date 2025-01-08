# class A:
#     """Class A"""
#     name_a = "class A is a parent"
#     is_name_class = True
#
#     def print_hello(self):
#         print("Hello from A")
#
# class B(A):
#     """Class B"""
#     name_b = "class B is a child"
#     is_name_class = False
#
#     def print_hello(self):
#         print("Hello from B")
#
#
# class C(B):
#     """Class C"""
#     pass
#
# test_ex = C()
# print(test_ex.name_a)
# print(test_ex.name_b)
# print(test_ex.is_name_class)
# test_ex.print_hello()
from itertools import count


# class Vehicle:
#     """It's a base class of Vehicles"""
#
#     def __init__(self, type, color, left_of_life=100):
#         self.type = type
#         self.color = color
#         self.left_of_life = left_of_life
#
#     def move(self):
#         print("Your vehicle is moving")
#
#
#     def fix(self):
#         if self.left_of_life <= 50:
#             print(f"{self.type} need to fix")
#         else:
#             print(f"Your {self.type} is good")
#
#
#
# class Car(Vehicle):
#     """Class Car"""
#     def __init__(self, type, color, eft_of_life, cost=0):
#         super().__init__(type, color, eft_of_life)
#         self.cost = cost
#
#     def move(self):
#         print(f"{self.color} {self.type} is driving")
#         print(f"Cost of this car: {self.cost}")
#
# class Bicycle(Vehicle):
#     """Class Bicycle"""
#     def __init__(self, type, color, eft_of_life, count_of_wells):
#         super().__init__(type, color, eft_of_life)
#         self.count_of_whells = count_of_wells
#
#     def move(self):
#         print("You are so fast")
#
# car_1 = Car("car", "black", 70, 10000)
# car_1.move()
# car_1.fix()
# bicycle_1 = Bicycle("road_bicycle", "blue", 30, 2000)
# bicycle_1.move()
# bicycle_1.fix()





# class Counter:
#     """Count of something"""
#     def __init__(self, count_obj, type_obj, max_elements):
#         self.count_obj = count_obj
#         self.type_obj = type_obj
#         self.max_elements = max_elements
#
#     def counter(self):
#         print(f"Type of object: {self.type_obj}")
#         if isinstance(self.count_obj, (list, dict, str, type)):
#             count = len(self.count_obj)
#             if count > self.max_elements:
#                 print("Count elements of your object more than need")
#                 print(f"More on {count - self.max_elements}")
#             else:
#                 print(f"Count of elements : {count}")
#         else:
#             print("Your object must be iterable")
#
#     def get_attrs(self):
#         print(self.__dict__)
#
#     def set_attr(self, attr, value):
#         print(attr, value)
#         if hasattr(self, attr):
#             setattr(self, attr, value)
#         else:
#             print("check your attrs")
#
# class ListElements(Counter):
#     """Class for list elements"""
#     def __init__(self, count_obj, type_obj, max_elements):
#         super().__init__(count_obj, type_obj, max_elements)
#         pass
#
#     def counter(self):
#         super().counter()
#
#         print("Operation was ended")
#
#
#     def get_attrs(self):
#         super().get_attrs()
#         print("Operation was ended")
#
# list_ex = ListElements([1, 2, 3, 4], list, 10)
# list_ex.counter()
# list_ex.get_attrs()
# list_ex.set_attr("count_obj", [1, 2, 3, 4, 5, 6])








class BaseInterface:
    """Base class"""
    def __init__(self):
        pass

    def get_attrs(self):
        pass

    def print_mode(self):
        pass

    def count_of_price(self):
        pass

    def call_to_support(self):
        pass


class ShopInterface(BaseInterface):
    """Interface of our site"""
    def __init__(self, number, model, price):
        super().__init__()
        self.number = number
        self.model = model
        self.price = price

    def print_model(self):
        print(f"Model of site: {self.model}")

    def count_of_price(self):
        print(f"Count of site: {self.price ** 2}")

    def call_to_support(self):
        print(f"Number of support is: {self.number}")
        print(f"You can call from 8am to 19pm")


class AppInterface(BaseInterface):
    """Interface of our application"""
    def __init__(self, number, model, price):
        super().__init__()
        self.number = number
        self.model = model
        self.price = price

    def print_model(self):
        print(f"Model of application: {self.model}")

    def count_of_price(self):
        print(f"Count of application: {self.price ** 2}")

    def call_to_support(self):
        print(f"Number of support is: {self.number}")
        print(f"You can call from 8am to 19pm")

site_user = ShopInterface(12345, "shop", 1000)
app_user = AppInterface(12345333, "android", 5000)\


for user in (site_user, app_user):
    user.print_model()
    user.count_of_price()
    user.call_to_support()
    print("---->")
