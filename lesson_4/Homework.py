print('Козацького здоровья! Ну що, почнемо?')
first_question = input('>')
while first_question != 'Привіт' or 'Хай' or 'Доброго дня':
    print('Дуже цікаво, але, нажаль, нічого не зрозуміло :(')
    if first_question == 'Привіт' or 'Хай' or 'Доброго дня':
        print('Доброго вечора, я бот з України!')
    break
second_question = input('>')
second_question_frases = 'Як справи? / Що робиш? / Чим займаєшся?'
while second_question  not in second_question_frases:
    print('Дуже цікаво, але, нажаль, нічого не зрозуміло :(')
    if second_question in second_question_frases:
        print('Вчусь програмувати на Python!')
    break
third_question_frases = ['Фільм', 'Кінотеатр', 'Серіал']
third_question = input('>')
while third_question not in third_question_frases:
    print('Дуже цікаво, але, нажаль, нічого не зрозуміло :(')
    if third_question == 'Фільм':
        print('Рекомендую подивитися "Веном" виключно українською мовою, дуже файний переклад!=)')
    if third_question == 'Кінотеатр':
        print('Зараз не найкращий час для відвідування кінотеатрів, краще йди провітри свій мозок на свіжому повітрі, '
              'воно доречі поки що БЕЗКОШТОВНЕ!=)')
        if third_question == 'Серіал':
            print('Ну тут все просто, подивісь "Король Талси" зі Сільвестром Сталоне у головній ролі, старикашка не '
                  'погано так віконує роль рішали=)')
            break
four_question_frases = ['Бувай', 'Надобраніч', 'Гудбай', 'До зустрічі']
four_question = input('>')
while four_question not in four_question_frases:
    print('Дуже цікаво, але, нажаль, нічого не зрозуміло :(')
    if four_question in four_question_frases:
        print("Побачимось у мережі, I'll be back")
    break

