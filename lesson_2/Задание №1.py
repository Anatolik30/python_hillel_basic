from math import pi
num_1 = 0
start = input('Укажите единицу конвертации Градус или Радиан?')
num_0 = float(input('Введите значение'))
if start == 'Градус' or 'Радиан':
    if start == 'Градус':
        num_1 = num_0 * (180 / pi)
        print(round(num_1, 5))
    elif start == 'Радиан':
        num_1 = num_0 * (pi / 180)
        print(round(num_1, 5))
    else:
        print('Введите единицу конвертации: Градус или Радиан')