class User:

    def __init__(self, name, email, password):
        self.__name = name
        self.__email = email
        self.__password = password

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def get_password(self):
        return self.__password

    def set_name(self, value):
        self.__name = value
        print(f"name: {value}")

    def set_email(self, value):
        self.__email = value
        print(f"email: {value}")

    def set_password(self, value):
        self.__password = value
        print(f"password: {value}")



user = User("Alisa", "alisa@gmail.com", "alisa12345")
print(user.get_name())
user.set_name("Lusia")
print(user.get_email())
user.set_email("lusia@gmail.com")
print(user.get_password())
user.set_password("lusia12345")





# class User:
#
#     def __init__(self, name, email, password, year):
#         self.__name = name
#         self.__email = email
#         self.__password = password
#         self.year = year
#
#     @property
#     def name(self):
#         return self.__name
#
#     @property
#     def email(self):
#         return self.__email
#
#     @property
#     def password(self):
#         return self.__password
#
#
#     @name.setter
#     def name(self, value):
#         self.__name = value
#         print(f"name: {value}")
#
#     @email.setter
#     def email(self, value):
#         self.__email = value
#         print(f"email: {value}")
#
#     @password.setter
#     def password(self, value):
#         self.__password = value
#         print(f"password: {value}")
#
#
# user = User("Alisa", "alisa@gmail.com", "alisa12345")
#
# print(user.name)
# user.name= "Katya"
#
# print(user.email)
# user.email = "error"
#
# print(user.password)
# user.password = "12345"