num_0 = float(input('Введите предыдущие показания: '))
num_1 = float(input('Введите текущие показания: '))
tax = float(input('Введите тариф: '))
price = round((num_1 - num_0) * tax, 2)  # Рассчет суммы к оплате по тарифу и показаниям.
print('К оплате: ', price, 'грн.')
