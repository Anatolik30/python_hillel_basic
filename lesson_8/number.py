def prost():
 while True:
    income = input('Enter number')
    try:
        income = int(income)
    except ValueError:
        print(
            "Некоректне введення. Будь ласка, введіть число ")
    if income in numbers:
        print(True)
    else:
        print(False)


if __name__ == '__main__':
    numbers = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101}
    prost()



