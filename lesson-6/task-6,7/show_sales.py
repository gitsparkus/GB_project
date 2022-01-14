import sys
from decimal import Decimal

SALES_FILE = 'bakery.csv'

start = '1'
finish = '0'
# Чтение переданных параметров
if len(sys.argv) > 1:
    start = sys.argv[1]
    if len(sys.argv) > 2:
        finish = sys.argv[2]

# Если парамтры - целые числа
if start.isnumeric() and finish.isnumeric():
    start = int(start)
    finish = int(finish)
    # Количество строк, кторые необходимо показать
    row_count = finish - start + 1
    # Если есть что показывать, или нужно показать весь файл
    if row_count > 0 or finish == 0:
        with open(SALES_FILE, 'r', encoding='UTF-8') as sales_f:
            # Установка курсора на старт. 18 - это по формату 16 символов числа + перевод строки
            sales_f.seek((start - 1) * 18)
            i = 1
            # Пока есть что показывать
            while i <= row_count or finish == 0:
                if sale := sales_f.readline().strip():
                    print(Decimal(sale))
                    i += 1
                else:
                    break
    else:
        print('Ошибка! Второе число должно быть больше первого')
        sys.exit()
else:
    print('Ошибка! Параметры должны быть целыми числами больше нуля!')
    sys.exit()
