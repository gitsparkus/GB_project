"""
1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
до минуты: <s> сек;
до часа: <m> мин <s> сек;
до суток: <h> час <m> мин <s> сек;
* в остальных случаях: <d> дн <h> час <m> мин <s> сек.
"""

duration = input('Продолжительность, сек (-1 для тестирования по списку):')  # запрос продолжительности от пользователя

if duration == '-1':  # Если введено -1, то запускаем в режиме тестирования
    duration_list = ['53', '153', '4153', '400153', '1.2']
else:
    duration_list = [duration, ]

for duration in duration_list:
    if duration.isnumeric():  # если введено целое число
        seconds_remainder = int(duration)
        days, seconds_remainder = divmod(seconds_remainder, 86400)  # дни, в seconds_remainder записывается остаток
        hours, seconds_remainder = divmod(seconds_remainder, 3600)  # часы, в seconds_remainder записывается остаток
        minutes, seconds_remainder = divmod(seconds_remainder, 60)  # минуты, в seconds_remainder записывается остаток

        # Учитывается вывод нулевых значений, если предыдуший интервал определен. Например, 60 вернет - 1 мин 0 сек
        # по заданию кажется, что нужно делать именно так
        result = f'{days} дн ' if days else ''  # есть дни - добавляем в результат
        result += f'{hours} час ' if hours or result else ''  # есть часы или результат не пустой - добавляем в результат
        result += f'{minutes} мин ' if minutes or result else ''  # есть минуты или результат не пустой - добавляем в результат
        result += f'{seconds_remainder} сек'  # добавляем секунды в результат
        print(f'{duration}:', result)
    else:  # если пользователь ввел не целое число
        print(f'{duration}:', 'Ошибка! Введенное значение не является целым числом!')
