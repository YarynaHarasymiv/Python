#Списки

# a = [1, 2, 3, 4, 5]
# b = ["apple", "banana", "cherry"]
#
# print(a[0], a[1], a[-1])
# print(b[1])
#
#
# print(a[1:4], a[::2])
# print(b[::2])
#
# print(a[::-1])
# print(b[::-1])
# print(a[3::-2])
#
#
#
#
# a = [1, 2, 3, 4, 5]
# b = ["apple", "banana", "cherry"]
#
# a.append(6)
# b.append("tomato")
# print(a)
# print(b)
#
# a.insert(3, 7.4)
# b.insert(3, "bottle")
# print(a)
# print(b)
# a.remove(7.4)
# b.remove("bottle")
# print(a)
# print(b)
#
#
# a.pop()
# b.pop()
# print(a, b, "->")
#
# last_elem_1 = a.pop()
# last_elem_2 = b.pop()
# print(last_elem_1, last_elem_2, "--->")
#
# last_elem_1 = a.pop(0)
# last_elem_2 = b.pop(0)
# print(last_elem_1, last_elem_2, "------>")
# print(a)
# print(b)
#
# print(a.index(3), b.index("banana"))
#
# a.extend([5, 5, 5])
# b.extend(["cherry", "banana", "banana"])
# print(a.count(5), b.count("banana"), b.count("cherry"))
#
# a.append(6)
# b.append("tomato")
#
# print(a, b, "------->")
#
#
# a.sort(reverse=True)
# b.sort()
# print(a, b)
# a.reverse()
# b.reverse()
# print(a, b, "------->")
#
#
#
#Кортежі
#
#
# a = (1, 2, 3, 4, 5, 5, 4)
# print(a[0], a[1], a[2])
# print(a[:2], a[-2:])
#
# print(a.count(5), a.count(4))
# print(a.index(4))




#Словники

#
# test_dict = {"user": "Oleg", "age": 21, "country": "Poland"}
# print(test_dict["user"], test_dict["age"], test_dict.get("country"))
# print(test_dict.get("animal", "key not found"))
# test_dict["age"] = 30
# print(test_dict["age"])
# test_dict["animal"] = "cat"
# print(test_dict["animal"])
# print(test_dict)
# animal = test_dict.pop("animal")
# print(test_dict)
# print(animal)

test_dict = {"user": "Oleg", "age": 21, "country": "Poland"}
copy_test = test_dict.copy()
test_dict.clear()
print(test_dict)
print(copy_test)

for key, value in copy_test.items():
    print(f"Key:{key}, Value: {value}")
# for item in copy_test:
#     print(item, "------>")
# for item in copy_test.values():
#         print(item)


wrong_key = copy_test.pop("currency", "key not found")
print(wrong_key)

dict_update = {"new_role": "admin", "salary": 10000}
copy_test.update(dict_update)
print(copy_test)