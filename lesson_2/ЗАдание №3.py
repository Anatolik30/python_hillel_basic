coming = float(input('Введите сумму прихода: '))
tax_rate = float(input('Введите процентную ставку: '))
amount_tax = round(coming / 100 * tax_rate)     # Рассчет суммы процентной ставки
profit = round(coming - amount_tax)             # Расчет чистой прибыли
print('Сумма налога равна: ', amount_tax, 'грн.')
print('Чистая прибыль равна: ', profit, 'грн.')
