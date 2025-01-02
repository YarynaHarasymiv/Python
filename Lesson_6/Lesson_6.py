# class Person:
#     """Class for creation person"""
#     name = "Tom"
#     age = 18
#     high = 180
#
# print(Person.name, Person.age)
# Person.age = 50
# print(Person.name, Person.age)
# print(Person.__dict__)
#
# person_1 = Person()
# print(person_1)
# print(person_1.name, person_1.age, person_1.high)
#
# person_2 = Person()
# print(person_2)
# print(person_2.name, person_2.age, person_2.high)
#
# person_1.is_animal = False
# print(person_1.__dict__)
# print(Person.__dict__)
# print(person_2.__dict__)
#
# print(getattr(person_1, "name"))
# print(getattr(person_1, "where_is", False))
#
# person_1.age = 59
# person_1.color = "black"
# print(person_1.__dict__)
#
# setattr(person_1, "high", 100)
# print(person_1.high)
# print(person_1.__dict__)
#
# print(hasattr(person_1, "name"))
# print(hasattr(person_1, "where_is"))
#
# del Person.high
# print(Person.__dict__)
# print(hasattr(Person, "high"))
#
# delattr(Person, "age")
# print(Person.__dict__)
# print(hasattr(Person, "age"))









# class Person:
#     """Class for creation person"""
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def print_attrs(self):
#         print(f">>>> {str(self)} <<<<")
#         print(self.name, self.age)
#
#
# person_1 = Person("Tom", 18)
# print(person_1)
# person_1.print_attrs()
#
# person_2 = Person("Oleg", 50)
# print(person_2)
# person_2.print_attrs()







class Point:
    """Class for create and set coords"""
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.get_attrs()
        self.check_coords()

    def check_coords(self):
        for attr in self.__dict__:
            if getattr(self, attr, False) < 0 and not isinstance(self.__dict__[attr], str):
                print("Coord can't be less than 0")
                setattr(self, attr, 0)
            elif getattr(self, attr, False) > 100 and not isinstance(self.__dict__[attr], str):
                print("Coord can't be great than 100")
        print(self.__dict__)

    def get_attrs(self):
        print(self.__dict__)

    def set_attrs(self, x ,y, z):
        self.x = x
        self.y = y
        self.z = z
        self.check_coords()
        print(self.__dict__)

coord1 = Point(-1, 101, 50)
print("------------->")
coord1.set_attrs(1000, 1000, -5)