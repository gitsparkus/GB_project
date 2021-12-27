import requests
from datetime import  datetime
from decimal import Decimal


def currency_rates(valute_code: str) -> dict:
    result_dict = {'date': None, 'rate': None}

    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    response_content = response.text

    if response_content.find('Date="') > 0:
        date_str = response_content.split('Date="')[1]
        date_str = date_str.split('"')[0]
        result_dict['date'] = datetime.strptime(date_str, '%d.%m.%Y')

    if response_content.find(valute_code.upper()) > 0:
        content_str = response_content.split(valute_code.upper())[1]
        content_str = content_str.split('<Value>')[1]
        content_str = content_str.split('</Value>')[0]
        result_dict['rate'] = Decimal(content_str.replace(',', '.'))

    return result_dict


if __name__ == '__main__':
    print(currency_rates('USD'))
    print(currency_rates('eur'))
