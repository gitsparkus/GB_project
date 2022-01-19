"""
Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения извлекает имя пользователя и
почтовый домен из email адреса и возвращает их в виде словаря. Если адрес не валиден, выбросить исключение ValueError.
Пример:
>> email_parse('someone@geekbrains.ru')
{'username': 'someone', 'domain': 'geekbrains.ru'}
>> email_parse('someone@geekbrainsru')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  ...
    raise ValueError(msg)
ValueError: wrong email: someone@geekbrainsru

Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном выражении; имеет ли смысл в
данном случае использовать функцию re.compile()?
"""
import re

# В имени пользователя допускаем только буквы латинского алфавита, подчеркивания, точки, минусы
# начинается и заканчивается обязательно цифрой или буквой
# после имени обязательно собака и в конце имя домена
# домен содержит хотя бы одну букву или цифру, потом точка и от 2 до бесконечности букв
RE_EMAIL = re.compile(
    r'^(?P<username>[0-9a-zA-Z][0-9a-zA-Z_.\-]+[0-9a-zA-Z])@(?P<domain>[0-9a-zA-Z]+\.[a-zA-Z]{2,})$')


def email_parse(email):
    if email_dict := RE_EMAIL.match(email):
        return email_dict.groupdict()
    else:
        raise ValueError(f'wrong email: {email}')


print(email_parse('so1m.e_on-e@geekb2rains.ru'))
