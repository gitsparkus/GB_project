import os
import shutil

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'my_project')
TEMPLATE_PATH = os.path.join(ROOT, 'templates')


# Функция создает папку, если она еще не существует
def make_folder(full_path):
    try:
        os.mkdir(full_path)
    except FileExistsError as e:
        pass  # print(f'Каталог "{full_path}" уже существует.')


# Создаем общую папку templates
make_folder(TEMPLATE_PATH)

# Проходим рекурсивно по всем папкам, начиная от корневой
for (dir_path, dir_names, filenames) in os.walk(ROOT):
    # Если в пути есть слово templates и это не общая папка для шаблонов
    if 'templates' in dir_path and TEMPLATE_PATH not in dir_path:
        # Перебираем все файлы в папке
        for filename in filenames:
            # Если это html
            if filename.lower().endswith('.html'):
                # Собираем целевой путь из пути к общей папке и имени папки, в которой находится текущий файл
                new_path = os.path.join(TEMPLATE_PATH, os.path.basename(dir_path))
                # Создаем новую папку
                make_folder(new_path)
                # Копируем файл в новую папку, не выдавая ошщибку, если он уже есть
                try:
                    shutil.copy(os.path.join(dir_path, filename), os.path.join(new_path, filename))
                except shutil.SameFileError as e:
                    pass  # print(f'Файл "{os.path.join(new_path, filename)}" уже существует.')
