income = input('Enter string: \n>')     # Ввод пользователя
punctuaition = '.,!?:;"-_—'     # Перечень знаков препинания
text = income.lower()       # Перевод в нижний регистр
text = text.strip()         # Удаление пробелов и табуляций по краям
for i in text.split():          # Цикл для построения списка и удаления знаков пунктуации
    print(i.strip(punctuaition), end=' ')   # Вывод списка без переноса строки и без знаков препинания
mirrow_text = text[::-1]        # Переворачивание строки для проверки на полиндромность
if text == mirrow_text:         # Условие если полимндомный
    print(' - string is Palindrome')        # Вывод
else:       # Условие для не полиндровности
    print(" - string is't Palindrome")      #Вывод
