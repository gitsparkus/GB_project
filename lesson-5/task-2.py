"""
Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield.
"""

n = input('Введите n:')
if n.isnumeric():
    n = int(n)
    odd_generator = (x for x in range(1, n + 1) if x % 2 != 0)
    print(next(odd_generator))
    print(next(odd_generator))
    print(next(odd_generator))
    print(next(odd_generator))
else:
    print('n должно быть целым числом!')
