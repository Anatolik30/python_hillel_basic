import sys  # модуль для завершения программы
from colorama import Fore, init  # модуль для изменения цвета текста

init(autoreset=True)  # возвращение цвета по умолчанию после применения цвета


def command():
    """
    Функція вибору команди
    """
    income = ''
    while income not in key_words:
        income = input(Fore.BLUE + 'Enter the command please: \n>').lower()
        if income == 'add':
            add_note()
        elif income == 'earliest':
            earliest_note()
        elif income == 'latest':
            latest_note()
        elif income == 'longest':
            longest_note()
        elif income == 'shortest':
            shortest_note()
        elif income == 'delete':
            delete_note()
        elif income == 'exit':
            sys.exit('See you later!')  # завершаем программу
        else:
            print('Enter one of the commands below, for EXIT enter', Fore.CYAN + "'exit'")
            for key, value in command_notations.items():  # Выводим список команд с разными цветами для ключей и
                # значений через цикл For
                print(Fore.GREEN + str(key), Fore.YELLOW + str(value))


def add_note():
    """
    Функція добавлення заміток
    """
    if open('content.txt', 'a', encoding='utf-8'):
        base = open('content.txt', 'a', encoding='utf-8')
        add_new = input('Enter your notes please: \n>')
        base.write(f'* {add_new} \n')  # Добавление заметок в список
        base.close()
    else:
        print('Can not open file.')
    command()  # Визов основної функції після кожної операції


def delete_note():
    """
    Функция для видалення нотаток
    """
    global note
    delete = input(
        Fore.RED + 'Enter the FULL note for delete please: \n>')  # Для акцентування виділення друкується червоним
    if open('content.txt', mode='r', encoding='utf-8'):
        base = open('content.txt', mode='r', encoding='utf-8')
        lines = base.readlines()  # Разбиваем на список строк для прохода циклом
        for note in lines:
            if delete in note:
                for_del = lines.index(note)  # Находим индекс нужно строки заметки
                del lines[for_del]  # Удаляем по индексу
                base.close()  # Закрываем файл что бы открыть его для перезаписи.. Сам понимаю что это должно быть не
                # так, но как смог как говориться
                base = open('content.txt', mode='w', encoding='utf-8')  # Открыываем для перезаписи
                for line in lines:  # циклом перезаписываем наш файл с удаленной заметкой
                    base.write(str(line))
                print(Fore.RED + 'deleted')
                base.close()
        if delete not in note:
            print("This note wasn't found.")
    else:
        print('Can not open file.')
    command()  # Визов основної функції після кожної операції


def earliest_note():
    """
    Функія виводить збережені нотатки у хронологічному порядку - від найранішої до найпізнішої
    """
    if open('content.txt', 'r', encoding='utf-8'):
        base = open('content.txt', 'r', encoding='utf-8')
        for note_1 in base:
            print(note_1)
        base.close()
    else:
        print('Can not open file.')
    command()  # Визов основної функції після кожної операції


def latest_note():
    """
    Функція виведення збережених нотаток від найпізнішої до найранішої
    """
    if open('content.txt', 'r', encoding='utf-8'):
        base = open('content.txt', 'r', encoding='utf-8')
        lines = base.readlines()
        for note_1 in reversed(lines):
            print(note_1)
        base.close()
    else:
        print('Can not open file.')
    command()  # Визов основної функції після кожної операції


def longest_note():
    """
    Функція виведення збережених нотаток від найдовшої до найкоротшої
    """
    if open('content.txt', 'r', encoding='utf-8'):
        base = open('content.txt', 'r', encoding='utf-8')
        sorted_list = (sorted(base, key=len, reverse=True))
        for note_1 in sorted_list:
            print(note_1)
        base.close()
    else:
        print('Can not open file.')
    command()  # Визов основної функції після кожної операції


def shortest_note():
    """
    Функція іиіедення нотаток від найкоротшої до найдовшої
    """
    if open('content.txt', 'r', encoding='utf-8'):
        base = open('content.txt', 'r', encoding='utf-8')
        sorted_list = sorted(base, key=len)
        for note_1 in sorted_list:
            print(note_1)
        base.close()
    else:
        print('Can not open file.')
    command()  # Визов основної функції після кожної операції


if __name__ == '__main__':
    if not open('content.txt', 'r', encoding='utf-8'):
        print('Can not open file')
    base_note = open('content.txt', 'r', encoding='utf-8')
    command_notations = {
        'add': '- додати нотатку.',
        'earliest': '- виводить збережені нотатки у хронологічному порядку - від найранішої до '
                    'найпізнішої',
        'latest': ' - виводить збережені нотатки у хронологічному порядку - від найпізнішої до найранішої',
        'longest': ' - виводить збережені нотатки у порядку їх довжини - від найдовшої до найкоротшої',
        'shortest': ' - виводить збережені нотатки у порядку їх довжини - від найкоротшоїдо найдовшої'}
    key_words = ['add', 'earliest', 'latest', 'longest', 'shortest', 'delete']  # Словник ключових команд
    command()  # Визов основної функції для старту програми
