from note_dict import notes_list


def command():
    income = ''
    while income not in key_words:
        income = input('Enter the command please: \n>').lower()
        print(f' Enter one of the commands {key_words}')
        if income == 'add':
            add_note()
        if income == 'earliest':
            earliest_note()
        if income == 'lastest':
            lastest_note()
        if income == 'longest':
            longest_note()
        if income == 'shortest':
            shortest_note()


def add_note():
    """
    Функция добавления заметки
    :param user_promt:
    :return:
    """
    add_new = input('Enter your notes please: \n>')
    notes_list.append(add_new)
    command()


def earliest_note():
    """
    Функія виводить збережені нотатки у хронологічному порядку - від найранішої до найпізнішої
    """
    for note in notes_list:
        print(note)
    command()


def lastest_note():
    for note in notes_list:
        print(note[::-1])
    command()


def longest_note():
    print(sorted(notes_list, key=len, reverse=True))
    command()



def shortest_note():
    print(sorted(notes_list, key=len))
    command()

if __name__ == '__main__':

    key_words = ['add', 'earliest', 'lastest', 'longest', 'shortest']
    command()
