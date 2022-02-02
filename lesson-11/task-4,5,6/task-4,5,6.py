"""
Начать работу над проектом «Склад оргтехники». Создать класс, описывающий склад. А также класс «Оргтехника», который
будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом
классе определить параметры, общие для приведённых типов. В классах-наследниках реализовать параметры, уникальные для
каждого типа оргтехники.
Продолжить работу над предыдущим заданием. Разработать методы, которые отвечают за приём оргтехники на склад и передачу
в определённое подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других
данных, можно использовать любую подходящую структуру (например, словарь).
Продолжить работу над предыдущим заданием. Реализовать механизм валидации вводимых пользователем данных. Например, для
указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
"""
from prettytable import PrettyTable
from classes import CompanyDivision, Xerox, Printer, Scanner

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
    for val in MENU_DICT.values():
        table.add_row([val])
    print(table)


def print_divisions(goods=False):
    """Вывод на экран списка подразделений"""
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


def select_equipment(division):
    """Выбор оборудования в указанном подразделении"""
    print(division)
    while True:
        try:
            equipment_id = int(input('Введите номер оборудования:'))
            equipment = division.equipment[equipment_id]
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
            equipment_type = int(input('Тип оборудования:')) - 1
            return EQUIPMENT_LIST[equipment_type][0]
        except ValueError:
            print('\033[93mОшибка! Введите целое число!\033[0m')
        except IndexError:
            print(f'\033[93mОшибка! Оборудование такого типа не поддерживается!\033[0m')


def bool_input(ask_str: str):
    """Запрос и валидация логического значения"""
    while True:
        result = input(ask_str).lower()
        if result == 'y':
            return True
        elif result == 'n':
            return False
        else:
            print('Введено некорректное значение. Введите Y или N.')


warehouse = CompanyDivision('Основной склад')
main_office = CompanyDivision('Главный офис', False)
printer = Printer('MX12-T', 'Brother', '---', False, True)
scanner = Scanner('ScanX', 'Epson' '334422')
warehouse.receipt(printer)
warehouse.receipt(scanner)

while True:
    print_menu()
    current_menu = input('Введите номер пункта меню: ')
    if MENU_DICT.get(current_menu):
        if current_menu == '0':
            print_divisions()
            input('Для продолжения нажмите Enter...')
        if current_menu == '1':
            print_divisions(True)
            input('Для продолжения нажмите Enter...')
        if current_menu == '2':
            division = select_division()
            equipment_type = select_equipment_type()
            model = input('Модель:')
            manufacturer = input('Производитель:')
            serial_number = input('Серийный номер:')
            is_new = bool_input('Новый(Y/N)?:')
            if equipment_type == '1':
                print_color = bool_input('Цветной(Y/N)?:')
                new_equipment = Printer(model, manufacturer, serial_number, is_new, print_color)
            elif equipment_type == '2':
                scan_color = bool_input('Цветное сканирование(Y/N)?:')
                new_equipment = Scanner(model, manufacturer, serial_number, is_new, scan_color)
            elif equipment_type == '3':
                print_color = bool_input('Цветное копирование(Y/N)?:')
                scan_color = bool_input('Цветное сканирование(Y/N)?:')
                new_equipment = Xerox(model, manufacturer, serial_number, is_new, print_color, scan_color)
            division.receipt(new_equipment)
            print(division)
            input('Для продолжения нажмите Enter...')
        if current_menu == '3':
            print('Откуда:')
            division_from = select_division()
            if division_from.equipment:
                equipment_id = select_equipment(division_from)
                print('Куда:')
                division_to = select_division()
                division_from.move(equipment_id, division_to)
            else:
                input('В выбранном подразделении нет оборудования! Для продолжения нажмите Enter...')
        if current_menu == '4':
            if bool_input('Завершить работу программы(Y/N)?'):
                break
    else:
        input(f'Пункта меню {current_menu} не существует! Для продолжения нажмите Enter...')
