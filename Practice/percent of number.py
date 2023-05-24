number_1 = 0
number_2 = 0
while True:
    first_number = input('Enter first number: \n >')
    second_number = input('Enter second number: \n >')
    try:
        number_1 = float(first_number)
        number_2 = float(second_number)
        break
    except ValueError:
        print('Enter the flot or integer number')
print(f'number_1 = {number_1}, number_2 = {number_2}, percent = {number_2 * 100 // number_1}')
