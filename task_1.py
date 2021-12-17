"""
1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
до минуты: <s> сек;
до часа: <m> мин <s> сек;
до суток: <h> час <m> мин <s> сек;
* в остальных случаях: <d> дн <h> час <m> мин <s> сек.
"""

duration = input("Продолжительность (сек):")  # запрос продолжительности от пользователя
if duration.isnumeric():  # если введено целое число
    seconds_remainder = int(duration)
    days, seconds_remainder = divmod(seconds_remainder, 86400)  # дни, в seconds_remainder записывается остаток
    hours, seconds_remainder = divmod(seconds_remainder, 3600)  # часы, в seconds_remainder записывается остаток
    minutes, seconds_remainder = divmod(seconds_remainder, 60)  # минуты, в seconds_remainder записывается остаток
    seconds = seconds_remainder  # оставшиеся секунды

    # Сознательно сделан вывод нулевых значений, если предыдуший интервал определен. Например, 60 вернет - 1 мин 0 сек
    # по заданию кажется, что нужно делать именно так
    result = f'{days} дн ' if days else ''  # есть дни - добавляем в результат
    result += f'{hours} час ' if hours or result else ''  # есть часы или результат не пустой - добавляем в результат
    result += f'{minutes} мин ' if minutes or result else ''  # есть минуты или результат не пустой - добавляем в результат
    result += f'{seconds} сек'  # добавляем секунды в результат
    print(result)
else:  # если пользователь ввел не целое число
    print('Ошибка! Введенное значение не является целым числом!')

"""
пример тестирования алгоритма с использованием списка
"""
# duration_list = ['53', '153', '4153', '400153', '1.2']
#
# for duration in duration_list:
#     if duration.isnumeric():
#         seconds_remainder = int(duration)
#         days, seconds_remainder = divmod(seconds_remainder, 86400)
#         hours, seconds_remainder = divmod(seconds_remainder, 3600)
#         minutes, seconds_remainder = divmod(seconds_remainder, 60)
#         seconds = seconds_remainder  # оставшиеся секунды
#
#         result = f'{days} дн ' if days else ''
#         result += f'{hours} час ' if hours or result else ''
#         result += f'{minutes} мин ' if minutes or result else ''
#         result += f'{seconds} сек'
#         print(result)
#     else:
#         print('Ошибка! Введенное значение не является целым числом!')
