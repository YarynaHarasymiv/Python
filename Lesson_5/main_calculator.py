import calculator

while True:
    try:
        a = float(input("Введіть значення а: "))
        break
    except ValueError:
        print("Введіть коректне значення!")


while True:
    try:
        b = float(input("Введіть значення b: "))
        break
    except ValueError:
        print("Введіть коректне значення!")


while True:
    add_operation = input("Введіть операцію : +, -, *, /  ")
    if add_operation not in ["+","-", "*", "/"]:
        print("Некоректно введена операція")
    else:
        if add_operation == "+":
                add = calculator.add(a, b)
                print(add)
        elif add_operation == "-":
                subtract = calculator.subtract(a, b)
                print(subtract)
        elif add_operation == "*":
                multiply = calculator.multiply(a, b)
                print(multiply)
        elif add_operation == "/":
                divide = calculator.divide(a, b)
                print(divide)
        else:
            print("Введіть коректну операцію")
        break



