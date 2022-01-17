import os
import shutil

ROOT = './my_project'
TEMPLATE_PATH = os.path.join(ROOT, 'templates')


def make_folder(full_path):
    try:
        os.mkdir(full_path)
    except FileExistsError as e:
        pass  # print(f'Каталог "{full_path}" уже существует.')


make_folder(TEMPLATE_PATH)

for (dir_path, dir_names, filenames) in os.walk(ROOT):
    for filename in filenames:
        if filename.endswith('.html'):
            new_path = os.path.join(TEMPLATE_PATH, os.path.split(dir_path)[1])
            make_folder(new_path)
            try:
                shutil.copy(os.path.join(dir_path, filename), os.path.join(new_path, filename))
            except shutil.SameFileError as e:
                pass  # print(f'Файл "{os.path.join(new_path, filename)}" уже существует.')
