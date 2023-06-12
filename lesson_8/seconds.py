def read_user_number(user_prompt: str):
    """
    Функция на проверку ввода
    :param user_prompt: ввод пользователя
    :return: передача значения согласно проверке
     """
    while True:  # Цикл проверки ввода корректных данных
        income = input(f'{user_prompt}\n>')  # Ввод пользователя
        try:  # Проверка на целочисленный ввод и на правильность показаний
            income = int(income)
            return income
        except ValueError:
            print(f'Некорректные показания, введите целочисленные значения')


def convert_time():
    """
    Функция на конвертацию секунд в дни, часы, минуты
    """
    # Конвертация в дни и расчет остатка секунд после конвертации в дни
    day = divmod(value, 86400)
    resalt.update({'days': day[0]})  # Добавление в словарь знчения дней
    balance = int(day[1])  # остаток секунд после конвертации в дни

    # Конвертация в часы и расчет остатка секунд после конвертации в часы
    hour = divmod(balance, 3600)
    resalt.update({'hours': hour[0]})  # добавление в словарь значения часа
    balance = int(hour[1])  # остаток после конвертации часов

    # Конвертация в минуты и расчет остатка секунд после конвертации в минуты
    minute = divmod(balance, 60)
    resalt.update({'minutes': minute[0]})  # добавление в словарь значение минут
    balance = int(minute[1])  # остаток секунд после конвертации в минуты
    resalt.update({'seconds': balance})  # Добавление остатка секунд в словарь под ключем "seconds"


if __name__ == '__main__':
    resalt = dict()  # Словарь с результатами
    value = read_user_number("Enter your seconds -->")
    convert_time()
    print(resalt)
