from math import pi

num_1 = 0  # Результат
start = input('Укажите единицу конвертации Градус или Радиан: ')  # Выбор единицы конвертации
num_0 = float(input('Введите значение: '))
if start == 'Градус' or 'Радиан':
    if start == 'Градус':  # Условие вычисления для Градусов
        num_1 = num_0 * (180 / pi)
        print(round(num_1, 5))
    elif start == 'Радиан':  # Условие вычисления для Радиан
        num_1 = num_0 * (pi / 180)
        print(round(num_1, 5))
    else:
        print('Введите единицу конвертации: Градус или Радиан')  # в случае не правильного выборора единицы
        # конвертации выводится пользователю.
