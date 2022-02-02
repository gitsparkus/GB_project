"""
Реализовать проект «Операции с комплексными числами». Создать класс «Комплексное число». Реализовать перегрузку методов
сложения и умножения комплексных чисел. Проверить работу проекта. Для этого создать экземпляры класса (комплексные
числа), выполнить сложение и умножение созданных экземпляров. Проверить корректность полученного результата.
"""
import re


class ComplexError(Exception):
    pass


class Complex:
    RE_COMPLEX = re.compile(r'^(?P<real>[+-]?[0-9]+)(?P<imaginary>[+-][0-9]+)i$')

    def __init__(self, complex_str='0+0i'):
        if complex_dict := Complex.RE_COMPLEX.match(complex_str):
            self.real = int(complex_dict.groupdict()['real'])
            self.imaginary = int(complex_dict.groupdict()['imaginary'])
        else:
            raise ComplexError(f'Wrong complex number format {complex_str}. Example: 5+6i')

    def __str__(self):
        return f'{self.real}{"+" if self.imaginary >= 0 else ""}{self.imaginary}i'

    def __add__(self, other):
        result = Complex()
        result.real = self.real + other.real
        result.imaginary = self.imaginary + other.imaginary
        return result

    def __mul__(self, other):
        result = Complex()
        result.real = self.real * other.real - self.imaginary * other.imaginary
        result.imaginary = self.real * other.imaginary + self.imaginary * other.real
        return result


complex1 = Complex('-5+6i')
complex2 = Complex('1-3i')
print(complex1, complex2)
print(f'({complex1})+({complex2}) = {(complex1 + complex2)}')
print(f'({complex1})*({complex2}) = {(complex1 * complex2)}')
