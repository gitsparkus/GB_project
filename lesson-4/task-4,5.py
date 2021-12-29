"""
4. Написать свой модуль utils и перенести в него функцию currency_rates() из предыдущего задания. Создать скрипт, в
котором импортировать этот модуль и выполнить несколько вызовов функции currency_rates(). Убедиться, что ничего лишнего
не происходит.
5. * (вместо 4) Доработать скрипт из предыдущего задания: теперь он должен работать и из консоли. Например:
> python task_4_5.py USD
75.18, 2020-09-05
"""

from utils import currency_rates
from datetime import datetime
import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:  # Если передан хоть один параметр при запуске
        rate_dict = currency_rates(sys.argv[1])  # Выполняем функцию, передав ей первый параметр
        if rate_dict['rate']:  # Если вернулся словарь, в котором есть курс
            print(f'{round(rate_dict["rate"], 2)}, {datetime.strftime(rate_dict["date"], "%Y-%m-%d")}')
