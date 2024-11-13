# string = "Hello world!"
#
# if "Hello" not in string:
#     print("Hello in string")
# elif "world" in string:
#     print("World in string")
# else:
#     print("Hello not in string")
#
# a = 10
# b = 20
#
# if a == 11 and b == 20 :
#     print(a + b)
# else:
#     print("Wrong condition")
from email.message import tspecials
from locale import currency

# test_list = ["Hello", "test", 1, 2, 3]
#
# if "Hello" in test_list and 1  in test_list:
#     print("Hello 1")
# elif "test" in test_list and 4 not in test_list:
#     print("Test not 4")
# else:
#     print("Your conditions wrong")
#
# print("End of your code")





# a = 10
# b = 20
# c = "Chat is active"
# d = "Count of users"
# print(len(c))
# print(len(d))
#
# if len(c) >= b:
#     print(c)
# elif len(d) <= a:
#     print(d)
# else:
#     print("Wrong conditions")






# user_1 = {
#     "name": "Tome",
#     "age": 21,
#     "balance": 20000,
#     "currency": "USD",
#     "status": True
# }
# user_2 = {
#     "name": "John",
#     "age": 17,
#     "balance": 5000,
#     "currency": "EUR",
#     "status": False
# }
# user_3 = {
#     #"name": "Karina",
#     "age": 30,
#     "balance": 100000,
#     "currency": "UAH",
#     "status": True
# }
#
# list_of_currency = ["USD", "EUR", "UAH"]
#
# if user_3.get("name", None) and user_3["age"] >= 18 and user_3["status"]:
#     if user_3["balance"] >=10000 and user_3["currency"] in list_of_currency:
#         print(f"Hello! You can create balance account, welcome {user_3['name']}")
#     elif user_3["balance"] >= 1000 and user_3["currency"] in list_of_currency:
#         print("You need more money")
#     else:
#         print("Money critical not enough")
# elif not user_3.get("name", None):
#     print("Please, wright your account description")
# elif user_3["age"] < 18:
#     print("For registry balance account you have to be 18 year old")
# else:
#     print("Something went wrong")



# test_list = [1, 2, 3, 4, 5, 6]
#
# for num in test_list:
#     print(f"You got a {num}")


# a = 0
#
# while a < 10:
#     print(a, "-----------<")
#     a += 1


# test_list = [1, 2, 3, 4, 5]
#
# while len(test_list) < 10:
#     print(test_list)
#     test_list.append(3)


# test_list = ['test', 'python', 'code']
#
# for s in test_list:
#     print(s, '-->')
#     if s == 'test':
#         print(s)
#     elif s == 'python':
#         print(s)
#     else:
#         print(s)



a = 0
add_list = []

while len(add_list) < 10:
    print("len of list", len(add_list))
    add_list.append(a)
    a += 1
    if len(add_list) == 5:
        print("You are at the middle of the list")




