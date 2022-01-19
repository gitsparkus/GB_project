"""
Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные значения функции и выбрасывать
исключение ValueError, если что-то не так, например:
def val_checker...
    ...

@val_checker(lambda x: x > 0)
def calc_cube(x):
   return x ** 3

>> a = calc_cube(5)
125
>> a = calc_cube(-5)
Traceback (most recent call last):
  ...
    raise ValueError(msg)
ValueError: wrong val -5

Примечание: сможете ли вы замаскировать работу декоратора?
"""

from functools import wraps

MIN_VALUE = 0


def val_checker(check_func):
    def _validator(callback):
        @wraps(callback)
        def wrapper(*args):
            if check_func(args[0]):
                return callback(*args)
            else:
                raise ValueError(f'wrong val {args[0]}')

        return wrapper

    return _validator


@val_checker(lambda x: x >= MIN_VALUE)
def calc_cube(x):
    return x ** 3


a = calc_cube(0)
print(a)
a = calc_cube(5)
print(a)
a = calc_cube(-5)
print(a)
print(calc_cube.__name__)
