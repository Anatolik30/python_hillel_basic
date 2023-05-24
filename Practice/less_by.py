income_first = 0
income_second = 0
resalt = 0
while True:
    first_number = input('Enter the first number: \n >')
    second_number = input('Enter the second number: \n >')
    try:
        income_first += float(first_number)
        income_second += float(second_number)
        break
    except ValueError:
        print('Enter the float or integer numbers')
if income_first >= income_second:
    resalt = round(income_first // income_second, 2)
print(f'{income_second} less than {income_first} on {resalt} ')
if income_first <= income_second:
    resalt = round(income_second // income_first, 2)
print(f'{income_first} less than {income_second} on {resalt}')
