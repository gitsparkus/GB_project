"""
*(вместо 1) Написать регулярное выражение для парсинга файла логов web-сервера из ДЗ 6 урока nginx_logs.txt
(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) для получения информации
вида: (<remote_addr>, <request_datetime>, <request_type>, <requested_resource>, <response_code>, <response_size>),
например:
raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET /downloads/product_2 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.9.7.9)"'
parsed_raw = ('188.138.60.101', '17/May/2015:08:05:49 +0000', 'GET', '/downloads/product_2', '304', '0')

Примечание: вы ограничились одной строкой или проверили на всех записях лога в файле? Были ли особенные строки? Можно
ли для них уточнить регулярное выражение?
"""
import re

# так как формат файла предопределен, особых проверок на соответствие формату нет
RE_RAW = re.compile(
    (
        r'(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|[a-z0-9:]+)\s-\s-\s\[(?P<dt>.+)] "(?P<type>\w+) (?P<url>.+) .+" (?P<code>\d+) (?P<size>\d+)'))


def parse_raw(row):
    return RE_RAW.match(row).groups()


with open('nginx_logs.txt', 'r', encoding='UTF-8') as f:
    with open('result.txt', 'w', encoding='UTF-8') as result_f:
        for line in f:
            result_parse = parse_raw(line)
            print(result_parse)
            # print(result_parse, file=result_f)
