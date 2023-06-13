import os
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
        if income == 'earliest':
            earliest_note()
        if income == 'latest':
            latest_note()
        if income == 'longest':
            longest_note()
        if income == 'shortest':
            shortest_note()
        if income == 'delete':
            delete_note()
        if income == 'exit':
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
    base = open('content.txt', 'a', encoding='utf-8')
    add_new = input('Enter your notes please: \n>')
    base.write(f'{add_new}, \n')    # Добавление заметок в список
    base.close()
    command()  # Визов основної функції після кожної операції


def delete_note():
    """
    Функция для видалення нотаток
    """
    delete = input(Fore.RED + 'Enter the note for delete please: \n>')  # Для акцентування виділення друкується червоним
    base = open('content.txt', 'r+', encoding='utf-8')
    lines = base.readlines()
    for line in lines:
        if delete in lines:
            new_line = base.replace(f'{delete}\n', '')
            base = base.write(new_line)
            print(Fore.RED + 'deleted')
    else:
        print("This note wasn't found.")
        base.close()
    command()  # Визов основної функції після кожної операції


def earliest_note():
    """
    Функія виводить збережені нотатки у хронологічному порядку - від найранішої до найпізнішої
    """
    base = open('content.txt', 'r', encoding='utf-8').read()
    for note in base:
        print(base.read)
    command()  # Визов основної функції після кожної операції


def latest_note():
    """
    Функція виведення збережених нотаток від найпізнішої до найранішої
    """
    for note in reversed(base_note):
        print(note)
    command()  # Визов основної функції після кожної операції


def longest_note():
    """
    Функція виведення збережених нотаток від найдовшої до найкоротшої
    """
    sorted_list = (sorted(base_note, key=len, reverse=True))
    for note in sorted_list:
        print(note)
    command()  # Визов основної функції після кожної операції


def shortest_note():
    """
    Функція іиіедення нотаток від найкоротшої до найдовшої
    """
    sorted_list = sorted(base_note, key=len)
    for note in sorted_list:
        print(note)
    command()  # Визов основної функції після кожної операції


if __name__ == '__main__':
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
