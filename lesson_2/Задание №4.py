consumption = float(input('Укажите расход автомобиля на 100 км: '))  # Расход топлива
price = float(input("Стоимость 1 литра топлива?: "))                 # Цена за 1 литр
if consumption >= 12:                                                # Комментарий
    print("Дешевле будет на велосипеде!")
distance = float(input("Укажите расстояние: "))                      # Расстояние
if distance >= 150:                                                  # Комментарий
    print("Да, расстояние не для велосипеда!")
consumption_at_one = consumption / 100 * distance                    # Расход топлива на 1 км
travel_cost = consumption_at_one * price                             # Стоимость поездки
print('Стоимость поездки: ', round(travel_cost, 2), 'грн.')