# correct_passvord = "password123"
#
# user_password = input("Введіть пароль:")
# if user_password == correct_passvord:
#     print("Ви увійшли в систему")
# else:
#     print("Неправильний пароль")
#




# enter_password = "password"
#
# correct_password = "password123"
#
# if enter_password == correct_password:
#     print("Ви увійшли в систему")
# else:
#     print("Неправтльний пароль")







# # Встановлюємо номер дня тижня
# day_number = int(input("Введіть номер дня тижня (1-7): "))
#
# # Визначаємо назву дня тижня за номером
# if day_number == 1:
#     print("Понеділок")
# elif day_number == 2:
#     print("Вівторок")
# elif day_number == 3:
#     print("Середа")
# elif day_number == 4:
#     print("Четвер")
# elif day_number == 5:
#     print("П'ятниця")
# elif day_number == 6:
#     print("Субота")
# elif day_number == 7:
#     print("Неділя")
# else:
#     print("Помилка: Невірний номер дня")





# day_1 = {
#     "day_is": "Monday",
#     "number_of_day": 1
# }
# day_2 = {
#     "day_is": "Tuesday",
#     "number_of_day": 2
# }
# day_3 = {
#     "day_is": "Wednesday",
#     "number_of_day": 3
# }
# day_4 = {
#     "day_is": "Thursday",
#     "number_of_day": 4
# }
# day_5 = {
#     "day_is": "Friday",
#     "number_of_day": 5
# }
# day_6 = {
#     "day_is": "Saturday",
#     "number_of_day": 6
# }
# day_7 = {
#     "day_is": "Sunday",
#     "number_of_day": 7
# }
#
#
# number_of_day = [1, 2, 3, 4, 5, 6, 7]
# list_of_day = [day_1, day_2, day_3, day_4, day_5, day_6, day_7]
#
#
# day_number = 7
#
#
# for day in list_of_day:
#     if day["number_of_day"] == day_number:
#         print(day["day_is"], day["number_of_day"])
#     else:
#         print("day is wrong")



# a = 6
# n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for number in n:
#     suma = a*number
#     result = str(number) + " * " + str(a) + "=" + str(suma)
#     print(result)
#     # print(number, "*", a, "=", a*number)

# n_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# n = int(input("Введіть число (1-10): "))
# for num in n_1:
#     suma = n * num
#     result = str(n) + " * " + str(num) + "=" + str(suma)
#     print(result)



# list = []
#
# list.append(1)
# list.append(3)
# list.append(5)
#
# print(list)
# print(list[2])
# print(list.index(3))






#
# list_of_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print("Сума чисел:",sum(list_of_number))
#
# sum_of_number = sum(list_of_number)
# print("Сума чисел:",sum_of_number)



# number = int(input("Введіть число:"))
#
# factorial = 1
# for i in range(1, number + 1):
#     factorial *= i
#
# print(f"Факторіал числа {number} дорівнює:", factorial)





# a = 1
# b = 50
#
# for i in range(1, b + 1):
#     if i % 2 == 0:
#         print(i)



# for num in range(1, 51):
#     if all(num %i != 0  for i in range(2, num)):
#         print(num)




