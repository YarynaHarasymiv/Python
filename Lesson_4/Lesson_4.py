a = [1, 2, 3, 4, 5]
b = ["apple", "banana", "cherry"]

print(a[0], a[1], a[-1])
print(b[1])


print(a[1:4], a[::2])
print(b[::2])

print(a[::-1])
print(b[::-1])
print(a[3::-2])




a = [1, 2, 3, 4, 5]
b = ["apple", "banana", "cherry"]

a.append(6)
b.append("tomato")
print(a)
print(b)

a.insert(3, 7.4)
b.insert(3, "bottle")
print(a)
print(b)
a.remove(7.4)
b.remove("bottle")
print(a)
print(b)


a.pop()
b.pop()
print(a, b, "->")

last_elem_1 = a.pop()
last_elem_2 = b.pop()
print(last_elem_1, last_elem_2, "--->")

last_elem_1 = a.pop(0)
last_elem_2 = b.pop(0)
print(last_elem_1, last_elem_2, "------>")
print(a)
print(b)

print(a.index(3), b.index("banana"))

a.extend([5, 5, 5])
b.extend(["cherry", "banana", "banana"])
print(a.count(5), b.count("banana"), b.count("cherry"))

a.append(6)
b.append("tomato")

print(a, b, "------->")


a.sort(reverse=True)
b.sort()
print(a, b)
a.reverse()
b.reverse()
print(a, b, "------->")




