from math import sqrt
str_input = input('Введите числа')        # Целочисленные переменные
a, b, c = str_input.split()

d = (b ** 2 - 4 * a * c)                  # Формула
if d >= 0:                              # Если больше или равно 0`
    print('is bigger then 0')
    x1 = (-b + sqrt(d)) / (2 * a)
    x2 = (-b - sqrt(d)) / (2 * a)
    print(x1)
    print(x2)
else:
    print('Not, it is not')
