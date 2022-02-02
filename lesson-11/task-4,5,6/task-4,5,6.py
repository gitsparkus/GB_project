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
from classes import CompanyDivision, Xerox, Printer, Scanner
from func_ui import print_menu, MENU_DICT, print_divisions, select_division, select_equipment_type, bool_input, \
    select_equipment

warehouse = CompanyDivision('Основной склад')
try:
    main_office = CompanyDivision('Главный офис', False)
    shop = CompanyDivision('Магазин', 'Нет')
except ValueError as err:
    print(f'\033[93m{err}\033[0m')

printer = Printer('MX12-T', 'Brother', '---', False, True)
scanner = Scanner('ScanX', 'Epson', '334422')
warehouse.receipt(printer)
warehouse.receipt(scanner)

while True:
    print_menu()
    if current_menu := input('Введите номер пункта меню: '):
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
                print('Откуда перемещаем:')
                division_from = select_division()
                if division_from.equipment:
                    equipment_id = select_equipment(division_from)
                    print('Куда перемещаем:')
                    division_to = select_division()
                    division_from.move(equipment_id, division_to)
                else:
                    input('\033[93mВ выбранном подразделении нет оборудования! Для продолжения нажмите Enter...\033[0m')
            if current_menu == '4':
                if bool_input('Завершить работу программы(Y/N)?'):
                    break
        else:
            input(f'\033[93mПункта меню {current_menu} не существует! Для продолжения нажмите Enter...\033[0m')
