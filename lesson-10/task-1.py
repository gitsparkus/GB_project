"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

31 22
37 43
51 86

3 5 32
2 4 6
-1 64 -8

3 5 8 3
8 3 7 1

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для сложения двух объектов класса Matrix (двух матриц). Результатом
сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно. Первый элемент первой строки первой матрицы складываем с
первым элементом первой строки второй матрицы и пр.
"""


class Matrix:
    def __init__(self, list_of_lists):
        if isinstance(list_of_lists, list) and sum({isinstance(x, list) for x in list_of_lists}):
            if len({len(x) for x in list_of_lists}) == 1:
                self.__matrix = list_of_lists
            else:
                raise ValueError("Размеры списков должны быть одинаковыми!")
        else:
            raise ValueError("Матрица должны быть списком списков")

    def __str__(self):
        return '\n'.join([str(x) for x in self.__matrix])

    def __add__(self, other):
        if len(self.__matrix) != len(other.__matrix):
            raise ValueError("Размеры матриц должны быть одинаковыми!")
        return Matrix(
            [list(map(lambda x, y: x + y, self.__matrix[i], other.__matrix[i])) for i in range(len(self.__matrix))])


list1 = [[1, 2], [3, 4]]
list2 = [[5, 6], [7, 8]]

matrix1 = Matrix(list1)
matrix2 = Matrix(list2)

matrix3 = matrix1 + matrix2

print(matrix1, '\n')
print(matrix2, '\n')
print(matrix3)
