import sys
from decimal import Decimal

SALES_FILE = 'bakery.csv'

# Чтение параметров командной строки
row_num = ''
sales_sum = ''
if len(sys.argv) > 2:
    row_num = sys.argv[1]
    sales_sum = sys.argv[2]

# Меняем первую запятую на точку, чтобы дальше использовать класс Decimal
sales_sum = sales_sum.replace(',', '.', 1)
# Убираем первую точку в сумме, чтобы проверить что введено корректное число
if row_num.isnumeric() and int(row_num) > 0 and sales_sum.replace('.', '', 1).isnumeric():
    row_num = int(row_num)
    # Приводим сумму к формату. Форма - 16 символов, число округлено до 2 знаков
    sales_sum = str(round(Decimal(sales_sum), 2)).zfill(16)
    with open(SALES_FILE, 'r+', encoding='UTF-8') as sales_f:
        # Установка курсора на нужную строку. 18 - это по формату 16 символов числа + перевод строки
        sales_f.seek((row_num - 1) * 18)
        if sales_f.readline(): # Если есть строка
            # Возврат курсора на нужную строку. Так как курсор перешел на следующую
            sales_f.seek((row_num - 1) * 18)
            sales_f.write(sales_sum)
        else:
            print(f'Нет строки с номером {row_num}')
else:
    print('Ошибка! Номер записи должен быть целым положительным числом, а сумма целым или вещественным числом!')
