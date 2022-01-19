"""
Написать декоратор для логирования типов позиционных аргументов функции, например:
def type_logger...
    ...

@type_logger
def calc_cube(x):
   return x ** 3

>> a = calc_cube(5)
5: <class 'int'>

Примечание: если аргументов несколько - выводить данные о каждом через запятую; можете ли вы вывести тип значения
функции? Сможете ли решить задачу для именованных аргументов? Сможете ли вы замаскировать работу декоратора? Сможете ли
вывести имя функции, например, в виде:
>> a = calc_cube(5)
calc_cube(5: <class 'int'>)
"""

from functools import wraps


def type_logger(callback):
    @wraps(callback)
    def wrapper(*args, **kwargs):
        args_str = ', '.join(map(lambda x: f'{x}: {type(x)}', args))
        kwargs_str = ', '.join(map(lambda x: f'{x[0]}={x[1]}: {type(x[1])}', kwargs.items()))
        print('Позиционные аргументы:', args_str)
        print('Именованные аргументы:', kwargs_str)
        result = callback(*args, **kwargs)
        print('Результат:', result, type(result))
        print(f'{callback.__name__}({", ".join((args_str, kwargs_str))})')
        return result

    return wrapper


@type_logger
def calc_cube(x, *args, **kwargs):
    return x ** 3


a = calc_cube(3, 'Куб', named_arg=(1, 2, 3), named_arg2=False)

print(calc_cube.__name__)
