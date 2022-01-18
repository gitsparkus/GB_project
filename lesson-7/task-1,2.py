"""
Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
|--my_project
   |--settings
   |--mainapp
   |--adminapp
   |--authapp


Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?); как лучше хранить конфигурацию
этого стартера, чтобы в будущем можно было менять имена папок под конкретный проект; можно ли будет при этом расширять
конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?
*(вместо 1) Написать скрипт, создающий из config.yaml стартер для проекта со следующей структурой:
|--my_project
   |--settings
   |  |--__init__.py
   |  |--dev.py
   |  |--prod.py
   |--mainapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--mainapp
   |        |--base.html
   |        |--index.html
   |--authapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--authapp
   |        |--base.html
   |        |--index.html


Примечание: структуру файла config.yaml придумайте сами, его можно создать в любом текстовом редакторе «руками» (не
программно); предусмотреть возможные исключительные ситуации, библиотеки использовать нельзя.
"""

import os

ROOT = os.path.dirname(os.path.abspath(__file__))
CONFIG = os.path.join(ROOT, 'config.yaml')

path_list = []

with open(CONFIG, 'r', encoding='UTF-8') as config_f:
    for line in config_f:
        if not line.startswith('#'):  # Если строка не комментарий
            indent = line.count('   ') - 1  # Количество отступов
            # В элемент списка, соответсвующий количеству отступов, записываем текущую строку
            path_list[indent:] = [line.strip()]
            cur_path = os.path.join(*path_list)  # Получаем путь, соединяя все элементы списка
            fullpath = os.path.join(ROOT, cur_path.replace(':', ''))  # Соединяем путь с корневым, убирая все двоеточия
            if cur_path.endswith(':'):  # Если путь заканчивается двоеточием, значит это папка
                os.makedirs(fullpath, exist_ok=True)  # Создаем все папки пути, игнорируя ошибку, если папки уже есть
            else:  # Если двоеточия в конце нет, значит это файл
                with open(fullpath, 'x', encoding='UTF-8') as new_f:  # Создаем файл
                    pass
