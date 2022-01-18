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
