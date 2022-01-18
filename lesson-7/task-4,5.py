import os
import json

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'files')

dict_result = dict()
# Проходим рекурсивно по всем папкам, начиная от корневой
for (dir_path, dir_names, file_names) in os.walk(ROOT):
    # Перебираем все файлы в папке
    for entry in os.scandir(dir_path):
        if entry.is_file():
            # Ключ для словаря = 1 плюс столько нулей, сколько цифр в размере файла
            key_size = '1' + len(str(entry.stat().st_size)) * '0'
            # Расширение файла
            file_extension = os.path.splitext(entry.name)[1].lstrip('.')
            # Если такой ключ уже есть в словаре
            if key_size in dict_result:
                # Увеличиваем счетчик
                dict_result[key_size][0] += 1
                # Добавляем расширение в множество. Множество выбрано для того, чтобы элементы не повторялись
                dict_result[key_size][1].add(file_extension)
            # Если ключа еще нет в словаре
            else:
                # Добавляем ключ в словарь со значением по умолчанию. По умолчанию это список из двух элементов
                # (целое число для счетчика и множество для накопления расширений)
                dict_result[key_size] = [1, {file_extension}]

# Преобразуем словарь под формат, требуемый по условию. Значения - кортежи, множества преобразовывем в списки
dict_result = {k: (v[0], list(v[1])) for k, v in sorted(dict_result.items())}

print(dict_result)

# Запись результата в файл json
with open(f'{os.path.basename(ROOT)}_summary.json', 'w', encoding='UTF-8') as json_file:
    json.dump(dict_result, json_file, indent=4)
