import os
import shutil

ROOT = './my_project'
TEMPLATE_PATH = os.path.join(ROOT, 'templates')


def make_folder(full_path):
    try:
        os.mkdir(full_path)
    except FileExistsError as e:
        print(f'Каталог "{full_path}" уже существует.')


dict_of_path = {}
for (dirpath, dirnames, filenames) in os.walk(ROOT):
    for filename in filenames:
        if filename.endswith('.html'):
            if dirpath in dict_of_path:
                dict_of_path[dirpath].append(filename)
            else:
                dict_of_path[dirpath] = [filename]

make_folder(TEMPLATE_PATH)
for path, files in dict_of_path.items():
    new_path = os.path.join(TEMPLATE_PATH, os.path.split(path)[1])
    make_folder(new_path)
    for file in files:
        try:
            shutil.copy(os.path.join(path, file), os.path.join(new_path, file))
        except shutil.SameFileError as e:
            print(f'Файл "{os.path.join(new_path, file)}" уже существует.')
