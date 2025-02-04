# from enum import Enum
#
# class Product(Enum):
#     SHIRT = 1
#     TSHIRT = 2
#     PANT = 3
#
#
# class DiscountCalculator:
#     def __init__(self, product_type, cost):
#         self.product_type = product_type
#         self.cost = cost
#
#
#
#     def get_discount(self):
#         if self.product_type == Product.SHIRT:
#             return self.cost - (self.cost * 0.10)
#         elif self.product_type == Product.TSHIRT:
#             return self.cost - (self.cost * 0.15)
#         elif self.product_type == Product.PANT:
#             return self.cost - (self.cost * 0.20)
#
#
# dc_shirt = DiscountCalculator(Product.SHIRT, 100)
# print(dc_shirt.get_discount())
# dc_tshirt = DiscountCalculator(Product.TSHIRT, 200)
# print(dc_tshirt.get_discount())
# dc_pant = DiscountCalculator(Product.PANT, 300)
# print(dc_pant.get_discount())








from abc import ABC, abstractmethod, abstractclassmethod


class DiscountCalculator(ABC):

    @abstractmethod
    def get_discount_product(self):
        pass

class DiscountCalculatorShirt(DiscountCalculator):
    def __init__(self, cost):
        self.cost = cost

    def get_discount_product(self):
        return self.cost - (self.cost * 0.10)



class DiscountCalculatorTshirt(DiscountCalculator):
    def __init__(self, cost):
        self.cost = cost

    def get_discount_product(self):
        return self.cost - (self.cost * 0.15)



class DiscountCalculatorPant(DiscountCalculator):
    def __init__(self, cost):
        self.cost = cost

    def get_discount_product(self):
        return self.cost - (self.cost * 0.20)



dc_shirt = DiscountCalculatorShirt(100)
print(dc_shirt.get_discount_product())

dc_tshirt = DiscountCalculatorTshirt(1000)
print(dc_tshirt.get_discount_product())

dc_pant = DiscountCalculatorPant(500)
print(dc_pant.get_discount_product())


