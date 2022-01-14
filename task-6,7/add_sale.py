import sys
from decimal import Decimal

SALES_FILE = 'bakery.csv'

# Чтение параметров командной строки
if len(sys.argv) > 1:
    sales_sum = sys.argv[1]
else:
    sales_sum = input('Введите сумму продаж за день:')

# Меняем первую запятую на точку, чтобы дальше использовать класс Decimal
sales_sum = sales_sum.replace(',', '.', 1)
# Убираем первую точку, чтобы проверить что введено корректное число
if sales_sum.replace('.', '', 1).isnumeric():
    # Приводим данные к формату. Форма - 16 символов, число округлено до 2 знаков
    sales_sum = str(round(Decimal(sales_sum), 2)).zfill(16)
    # Открываем файл в режиме добавления и записываем данные
    with open(SALES_FILE, 'a+', encoding='UTF-8') as sales_f:
        sales_f.write(f'{sales_sum}\n')
else:
    print('Ошибка! Введенные данные должны быть целым или вещественным числом!')
