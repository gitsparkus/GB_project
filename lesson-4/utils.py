import requests
from datetime import datetime
from decimal import Decimal


def currency_rates(val_code: str) -> dict:
    result_dict = {'date': None, 'rate': None}
    val_code = val_code.upper()

    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    response_content = response.text

    if response_content.find('Date="') > 0:  # Если в ответе есть Date
        date_str = response_content.split('Date="')[1].split('"')[0]
        # Записать в результат дату, сконвертировав ее в тип DateTime
        result_dict['date'] = datetime.strptime(date_str, '%d.%m.%Y')

    if response_content.find(val_code) > 0:  # Если в ответе есть код валюты в верхнем регистре
        rate_str = response_content.split(val_code)[1].split('<Value>')[1].split('</Value>')[0]
        # Записать в результат курс, сконвертировав его в тип Decimal. Он больше подходид для работы с деньгами,
        # потому что при его использовании не теряются копейки и не появляются неожиданные дробные хвосты у чисел
        result_dict['rate'] = Decimal(rate_str.replace(',', '.'))

    return result_dict


if __name__ == '__main__':
    print(currency_rates('USD'))
    print(currency_rates('eur'))
