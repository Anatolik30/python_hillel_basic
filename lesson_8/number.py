def int_number(user_promt: str):  # Обьявление функции
    """
    Функция для определения является ли число простым
    :param user_promt:

    """
    # Цикл с проверкой на корректный ввод и пренадлежание числу к простому
    while True:
        income = input(f'{user_promt}\n')
        try:
            income = int(income)
            if income in numbers:
                print(f'{income} - True')
            if income not in numbers:
                print(f'{income} - False')
        except ValueError:
            print("Input Error.")


if __name__ == '__main__':
    # Кортеж с перечнем простіх чисел
    numbers = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}
    int_number('Enter the simple number: \n >')  # Вызов функции
