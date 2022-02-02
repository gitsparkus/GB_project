from classes import CompanyDivision
from prettytable import PrettyTable

MENU_DICT = {
    '0': '0. Показать список подразделений и складов',
    '1': '1. Показать наличие оборудования',
    '2': '2. Приход товара',
    '3': '3. Перемещение товара',
    '4': '4. Выход'
}

EQUIPMENT_LIST = [
    ['1', 'Принтер'],
    ['2', 'Сканер'],
    ['3', 'Ксерокс']
]


def print_menu():
    """Вывод на экран меню"""
    table = PrettyTable(['МЕНЮ'])
    table.align["МЕНЮ"] = "l"
    for item in MENU_DICT.values():
        table.add_row([item])
    print(table)


def print_divisions(goods=False):
    """
    Вывод на экран списка подразделений

    :param goods: Показывать наличие оборудования
    :return: None
    """
    for i, item in enumerate(CompanyDivision.get_divisions()):
        if goods:
            print(item)
        else:
            print(f'{i}. {item.name} ({item.type})')


def select_division():
    """Выбор подразделения"""
    print_divisions()
    while True:
        try:
            division_id = int(input('Введите номер склада:'))
            return CompanyDivision.get_divisions()[division_id]
        except ValueError:
            print('\033[93mОшибка! Введите целое число!\033[0m')
        except IndexError:
            print('\033[93mОшибка! Подразделения с таким номером не существует!\033[0m')


def select_equipment(division: CompanyDivision):
    """
    Выбор оборудования в указанном подразделении

    :param division: class CompanyDivision
    :return: int
    """
    print(division)
    while True:
        try:
            equipment_id = int(input('Введите номер оборудования:'))
            assert division.equipment[equipment_id]
            return equipment_id
        except ValueError:
            print('\033[93mОшибка! Введите целое число!\033[0m')
        except IndexError:
            print(f'\033[93mОшибка! Оборудования с таким номером не существует в подразделении {division.name}!\033[0m')


def select_equipment_type():
    """Выбор типа оборудования"""
    while True:
        try:
            for item in EQUIPMENT_LIST:
                print(f'{item[0]}. {item[1]}')
            return EQUIPMENT_LIST[int(input('Тип оборудования:')) - 1][0]
        except ValueError:
            print('\033[93mОшибка! Введите целое число!\033[0m')
        except IndexError:
            print(f'\033[93mОшибка! Оборудование такого типа не поддерживается!\033[0m')


def bool_input(ask_str: str):
    """
    Запрос и валидация логического значения

    :param ask_str: str. Строка запроса для input
    :return: bool
    """
    while True:
        result = input(ask_str).lower()
        if result == 'y':
            return True
        elif result == 'n':
            return False
        else:
            print('\033[93mВведено некорректное значение. Введите Y или N.\033[0m')
