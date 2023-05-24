resalt = 0
while True:
    input_number = input('Enter the number: \n>')
    try:
        resalt = int(input_number)
        break
    except ValueError:
        print('Enter integer number')
mirrow_number = resalt[::-1]
if resalt == mirrow_number:
    print(f'{input_number} is Palindrome')
else:
    print(f"{input_number} isn't Palindrome")
