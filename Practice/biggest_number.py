first_income = 0
second_income = 0
while True:
    first_number = input('Enter the first number: \n >')
    second_number = input('Enter the second number: \n >')
    try:
        first_income += float(first_number)
        second_income += float(second_number)
        break
    except ValueError:
        print('Enter the integer or float number ')
if first_income >= second_income:
    print(f'{first_income} is bigger then {second_income} more then {first_income - second_income}')
elif second_number >= first_number:
    print(f'{second_income} is bigger then {first_income} more than {second_income - first_income}')
