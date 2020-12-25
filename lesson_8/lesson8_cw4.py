"""
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника», который
будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом
классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры, уникальные для
каждого типа оргтехники.
"""


class WareHouse:
    def __init__(self, name):
        self.name = name
        pass


class OfficeEquipment:
    def __init__(self, name, price, make, model, store: 'WareHouse'):
        self.name = name
        self.store = store
        self.price = price
        self.make = make
        self.model = model

    def __str__(self):
        params = ''
        for key in self.__dict__:
            if key == 'store':
                params = f"{params}{key} : {self.__dict__[key].name} \n"
            else:
                params = f"{params}{key} : {self.__dict__[key]} \n"
        return params


class CopyMachine(OfficeEquipment):
    def __init__(self, price, make, model, double_sided, store):
        super().__init__('CopyMachine', price, make, model, store)
        self.double_sided = double_sided


class Printer(OfficeEquipment):
    def __init__(self, price, make, model, is_color, store):
        super().__init__('Printer', price, make, model, store)
        self.is_color = is_color


class Scanner(OfficeEquipment):
    def __init__(self, price, make, model, can_pdf, store):
        super().__init__('Scanner', price, make, model, store)
        self.can_pdf = can_pdf


if __name__ == "__main__":
    warehouse = WareHouse('base')
    office_tech = [Printer(10000, 'Hewlett-Packard', 'CX-500', True, warehouse),
                   Scanner(2000, 'Samsung', 'S500', False, warehouse),
                   CopyMachine(5000, 'Lenovo', 'CopyLeft', True, warehouse)]

    for el in office_tech:
        print(el)
