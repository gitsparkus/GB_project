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

MENU_DICT = {
    '1': '1. Показать список складов/подразделений и остатков оборудования',
    '2': '2. Приход товара',
    '3': '3. Перемещение товара',
    '4': '4. Выход'
}


def print_menu():
    print('----------------------------------')
    print('Меню системы:')
    for val in MENU_DICT.values():
        print(val)


def print_devisions(goods=False):
    for i, item in enumerate(CompanyDivision.get_divisions()):
        print(f'{i}. {item.name}')
        if goods:
            print(item)

def select_division():
    print_devisions()
    devision_id = None
    while devision_id not in range(len(CompanyDivision.get_divisions())):
        devision_id = int(input('Введите номер склада:'))
    return CompanyDivision.get_divisions()[devision_id]

warehouse = CompanyDivision('Основной склад')
main_office = CompanyDivision('Главный офис', False)
printer = Printer('MX12-T', 'Brother', '---', False, True)
scanner = Scanner('ScanX', 'Epson' '334422')
warehouse.receipt(printer, 3)
warehouse.receipt(scanner, 1)

while True:
    print_menu()
    current_menu = input('Введите номер пункта меню: ')
    if MENU_DICT.get(current_menu):
        if current_menu == '1':
            print_devisions(True)
            input('Для продолжения нажмите Enter...')
        if current_menu == '2':
            devision = select_division()
            type_eq = '0'
            while type_eq not in ('1', '2', '3'):
                type_eq = input('Тип оборудования(1-принтер,2-сканер,3-ксерокс):')
                if type_eq in ('1', '2', '3'):
                    model = input('Модель:')
                    manufacturer = input('Производитель:')
                    serial_number = input('Серийный номер:')
                    is_new = True if input('Новый(Y/N)?:') == 'Y' else False
                    if type_eq == '1':
                        print_color = True if input('Цветной(Y/N)?:') == 'Y' else False
                        new_eq = Printer(model, manufacturer, serial_number, is_new, print_color)
                    elif type_eq == '2':
                        scan_color = True if input('Цветное сканирование(Y/N)?:') == 'Y' else False
                        new_eq = Scanner(model, manufacturer, serial_number, is_new, scan_color)
                    elif type_eq == '3':
                        print_color = True if input('Цветное копирование(Y/N)?:') == 'Y' else False
                        scan_color = True if input('Цветное сканирование(Y/N)?:') == 'Y' else False
                        new_eq = Xerox(model, manufacturer, serial_number, is_new, print_color, scan_color)
                    devision.receipt(new_eq, 1)
                    print(devision)
                    input('Для продолжения нажмите Enter...')
        if current_menu == '3':
            print('Откуда:')
            devision_from = select_division()
            print(devision_from)

            print('Куда:')
            devision_to = select_division()

        if current_menu == '4':
            break
