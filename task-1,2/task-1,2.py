"""
Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt
(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) — получить список
кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:

[
...
('141.138.90.60', 'GET', '/downloads/product_2'),
('141.138.90.60', 'GET', '/downloads/product_2'),
('173.255.199.22', 'GET', '/downloads/product_2'),
...
]

* (вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего задания.
Примечания: спамер — это клиент, отправивший больше всех запросов; код должен работать даже с файлами, размер которых
превышает объем ОЗУ компьютера.
"""


# Генератор парсинга файла
def parse_file_generator(parse_file):
    for line in parse_file:
        remote_address = line.split(' ')[0]
        request_type = line.split(' ')[5].lstrip('"')
        requested_resource = line.split(' ')[6]
        yield remote_address, request_type, requested_resource


# Проверка работы генератора
with open('nginx_logs.txt', 'r', encoding='UTF-8') as f:
    for item in parse_file_generator(f):
        pass
        # input(item)

# Парсинг файла и формирование словаря, где ключи - ip, а значения - количество их повторений
spammers_dict = dict()
with open('nginx_logs.txt', 'r', encoding='UTF-8') as f:
    for item in parse_file_generator(f):
        if item[0] in spammers_dict:
            spammers_dict[item[0]] += 1
        else:
            spammers_dict[item[0]] = 1

# Фильтр возвращает список кортежей вида (спамер, количество запросов). На случай, если бедет несколько ip с одинаковым
# количеством запросов
spammers = list(filter(lambda x: x[1] == max(spammers_dict.values()), spammers_dict.items()))
print(spammers)
