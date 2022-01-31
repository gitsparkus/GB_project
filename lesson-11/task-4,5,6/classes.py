from prettytable import PrettyTable

class CompanyDivision:
    _divisions = []

    @classmethod
    def get_divisions(cls):
        return cls._divisions

    def __init__(self, name, is_warehouse=True):
        self._name = name
        self._equipment = []
        self.__is_warehouse = is_warehouse
        CompanyDivision._divisions.append(self)

    def receipt(self, equipment, quantity):
        self._equipment.append({'item': equipment, 'quantity': quantity})

    def move(self, equipment_id: int, division, quantity):
        if quantity == self._equipment[equipment_id]['quantity']:
            division._equipment.append(self._equipment.pop(equipment_id))
        elif quantity in range(1, self._equipment[equipment_id]['quantity']):
            self._equipment[equipment_id]['quantity'] -= quantity
            division._equipment.append({'item': self._equipment[equipment_id]['item'], 'quantity': quantity})
        else:
            raise ValueError

    def __str__(self):
        table = PrettyTable(['id', 'Наименование', 'Количество', 'Состояние'])
        for i, item in enumerate(self._equipment):
            table.add_row([i, str(item['item']), item['quantity'], item['item'].condition])
        return f'{str(table)}'

    @property
    def name(self):
        return self._name


class OfficeEquipment:
    _type = 'Equipment'

    def __init__(self, name, manufacturer, serial_number='---', is_new=True):
        self._name = name
        self._manufacturer = manufacturer
        self._serial_number = serial_number
        self._is_new = is_new

    def __str__(self):
        return f'{self._type} {self._manufacturer} {self._name}\nS/N: {self._serial_number}'

    @property
    def condition(self):
        return 'New' if self._is_new else 'Used'


class Printer(OfficeEquipment):
    _type = 'Принтер'

    def __init__(self, name, manufacturer, serial_number='---', is_new=True, print_color=False):
        super().__init__(name, manufacturer, serial_number, is_new)
        self._print_color = print_color


class Scanner(OfficeEquipment):
    _type = 'Сканер'

    def __init__(self, name, manufacturer, serial_number='---', is_new=True, scan_color=False):
        super().__init__(name, manufacturer, serial_number, is_new)
        self._scan_color = scan_color


class Xerox(OfficeEquipment):
    _type = 'Ксерокс'

    def __init__(self, name, manufacturer, serial_number='---', is_new=True, print_color=False, scan_color=False):
        super().__init__(name, manufacturer, serial_number, is_new)
        self._print_color = print_color
        self._scan_color = scan_color