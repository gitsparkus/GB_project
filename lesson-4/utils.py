import requests
from datetime import datetime
from decimal import Decimal


def currency_rates(val_code: str) -> dict:
    result_dict = {'date': None, 'rate': None}

    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    response_content = response.text

    if response_content.find('Date="') > 0:  # Если в ответе есть Date
        date_str = response_content.split('Date="')[1]  # разделить строку по Date и взять вторую часть
        date_str = date_str.split('"')[0]  # Разделить по " и взять первую часть

        # Записать в результат дату, сконвертировав ее в тип DateTime
        result_dict['date'] = datetime.strptime(date_str, '%d.%m.%Y')

    if response_content.find(val_code.upper()) > 0:  # Если в ответе есть код валюты в верхнем регистре
        content_str = response_content.split(val_code.upper())[1]  # разделить строку по коду валюты и взять 2 часть
        content_str = content_str.split('<Value>')[1]  # Разделить по тэгу <Value> и взять вторую часть
        content_str = content_str.split('</Value>')[0]  # Разделить по тэгу </Value> и взять первую часть

        # Записать в результат курс, сконвертировав его в тип Decimal. Он больше подходид для работы с деньгами,
        # потому что при его использовании не теряются копейки и не появляются неожиданные дробные хвосты у чисел
        result_dict['rate'] = Decimal(content_str.replace(',', '.'))

    return result_dict


if __name__ == '__main__':
    print(currency_rates('USD'))
    print(currency_rates('eur'))
