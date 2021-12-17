"""
Реализовать склонение слова «процент» во фразе «N процентов». Вывести эту фразу на экран отдельной строкой для каждого
из чисел в интервале от 1 до 100:
1 процент
2 процента
3 процента
4 процента
5 процентов
6 процентов
...
100 процентов
"""

for i in range(1, 101):
    # Рассматирваем только две последние цифры числа, чтобы алгоритм корректно работал на значениях больше 100
    last_two_digits = int(str(i)[-2:])
    last_digit = int(str(i)[-1])
    percent_word = ''

    if last_digit == 0 or last_digit in range(5, 10) or last_two_digits in range(11, 15):
        percent_word = 'процентов'
    elif last_digit == 1:
        percent_word = 'процент'
    elif last_digit in range(2, 5):
        percent_word = 'процента'
    print(i, percent_word)


