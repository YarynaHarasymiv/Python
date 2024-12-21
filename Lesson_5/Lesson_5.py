# def say_hello(username, age):
#     print(f"Hello {username} welcome to the club, buddy")
#     print(f"Your age is {age}, you are so beautiful")
#     print("------->")
#
# def print_numbers(start, stop):
#     for num in range(start, stop):
#         print(f"Current number is {num}")
#     print("------>")
#
# user_data = {"Dima": 25, "Sarah": 34, "Tom": 11}
# list_of_ranges = [(1, 10), (2, 9), (0, 10)]
#
# # for name, age in user_data.items():
# #     say_hello(name, age)
#
# for start_pos, stop_pos in list_of_ranges:
#     print_numbers(start_pos, stop_pos)


# print("------")
# def check_connection(username, count_tries, priority):
#     if priority >= 10:
#         finish = 5
#         for attemt in range(1, count_tries + 1):
#             if attemt == finish:
#                 print("Connect was successfully")
#                 break
#             print(f"Attemp: {attemt} to connect to {username}")
#
#     elif priority >= 5 and priority < 10:
#         finish = 3
#         for attemt in range(1, 6):
#             if attemt == finish:
#                 print("Connect was successfully")
#             print(f"Attwmp: {attemt} to connect to username")
#
#     else:
#         print("Your username has so low priority")
#
# check_connection(count_tries=10, username="Oleg", priority=100)

# import turtle
#
# def drowSquare(size, color):
#     turtle.speed(1)
#     turtle.color(color)
#     turtle.begin_fill()
#     def move(len):
#         turtle.forward(len)
#         turtle.left(90)
#     for _ in range(4):
#             move(size)
#     turtle.end_fill()
#
# drowSquare(100, "red")
# turtle.goto(200, 200)
# drowSquare(200, "blue")

