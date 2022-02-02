"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год». В
рамках класса реализовать два метода. Первый — с декоратором @classmethod. Он должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй — с декоратором @staticmethod, должен проводить валидацию числа, месяца и
года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""

import re
from datetime import datetime


class Date:
    RE_DATE = re.compile(r'^(?P<day>[0-9]{1,2})-(?P<month>[0-9]{1,2})-(?P<year>[0-9]{4})$')

    def __init__(self, date_str):
        self.date_str = date_str
        self.date = self.validation(date_str)

    @classmethod
    def parse_date_str(cls, date_str: str):
        if date_dict := cls.RE_DATE.match(date_str):
            return tuple(map(int, date_dict.groups()))
        return None

    @staticmethod
    def validation(date_str):
        try:
            if date_tuple := Date.parse_date_str(date_str):
                return datetime(date_tuple[2], date_tuple[1], date_tuple[0])
            else:
                raise ValueError('\033[93mСтрока не соответствует формату «день-месяц-год»\033[0m')
        except ValueError as err:
            print(f'\033[93m{err}\033[0m')

date1 = Date('28-12-2021')
print(date1.date)

date1 = Date('28-42-2021')
print(date1.date)

date1 = Date('28--2-2021')
print(date1.date)
