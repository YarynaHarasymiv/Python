# list = [1, 2, 3, 4, 5]
# list.append(10)
# list.append(20)
# print(list)
# list.remove(10)
# print("Результат списку:", list)
#
#
#
#
#
#
# list = [1, 2, 3, 4, 5]
# sum_list = sum(list)
# print("Сума чисел у списку :", sum_list)
#
#
#
#
#
#
# list = [1, 2, 3, 4, 5]
# duble_list = [n ** 2 for n in list]
# print("Список подвоєних чисел:", duble_list)
#
#
#
#
#
#
# #1
# tuple = ("apple", "banana", "orange")
# print(tuple[0])
# print(tuple[1])
# print(tuple[2])
#
# #2
# for i in tuple:
#     print(i)
#
#
#
#
#
#
# #1
# tuple = ("apple", "banana", "orange")
# print(tuple[0])
# print(tuple[1])
# print(tuple[2])
#
# #2
# for i in tuple:
#     print(i)
#
#
#
#
#
#
# number_1 = (1, 2, 3, 4, 5)
# number_2 = (6, 7, 8, 9, 10)
#
# join_of_numbers = number_1 + number_2
#
# print("Об'єднаний кортеж:", join_of_numbers)
#
#
#
#
#
#
# athlete = {
#     "name": "Ivan",
#     "age": "25",
#     "sport": "football",
#     "team": "Omega"
# }
#
# for key, value in athlete.items():
#     print(f"{key}:  {value}")
#
#
#
#
#
#
# books = {
#     "1984": "1949",
#     "Сім чоловіків Евелін Гю'го": "2015",
#     "Вкріті": "2017",
#     "9 листопада": "2019",
#     }
# books["Покинь якщо кохаєш"] = 2016
# print(books)
# print("------------->")
# for key, value in books.items():
#     print(f"{key}: {value}")
#
#
#
#
#
#
# countries = {
#     "Ukraine": "Kyiv",
#     "Poland": "Warshaw",
#     "France": "Parise"
# }
#
# cuntry = input("Введіть назву країни: ")
# capital = countries.get(cuntry)
# if capital:
#     print(f"Столиця {cuntry}: {capital}")
# else:
#     print("Такої країни немає у словнику.")
#
#
#
