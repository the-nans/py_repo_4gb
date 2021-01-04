"""
Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других
данных, можно использовать любую подходящую структуру, например словарь.

"""
from abc import ABC, abstractmethod


class WareHouse:
    """
    Я тут пока только параметры склада и статический метод печати отчета вписала. А так можно много всяких
    параметров наплодить, относящихся именно к сущности Склад
    Метод отчёта тут тоже лежит в основном потому, что документооборот - свойство предприятия, а не оборудования
    """

    def __init__(self, name, shipment_address='Default', phone='нет', contact_person='John Doe'):
        self.name = name
        self.shipment_address = shipment_address
        self.phone = phone
        self.contact_person = contact_person


class StoreHelper:
    """
    Набор статических методов для работы с классами Склад и Оргтехника+потомки.
    """

    @staticmethod
    def list(tech: list, store: 'WareHouse'):
        """
        Отчёт по содержимому склада в выбранной локации
        :param tech:
        :param store:
        :return:
        """
        report = f'Склад: {store.name} \n Адрес: {store.shipment_address} \n ' \
                 f'Телефон: {store.phone}\n' \
                 f'Завскладом: {store.contact_person}\n'
        for item in tech:
            if store.name in item.positions.keys() and item.positions[store.name] > 0:
                in_stock = list(item.positions.values())[list(item.positions.keys()).index(store.name)]
                report = \
                    f"""{report}Наименование: {item.name} {item.make}
    Модель: {item.model}
    Стоимость: {item.price}
    ===
    В наличии:
    ===
    {in_stock}\n"""
        return report


class DistributableWare(ABC):
    __store: WareHouse

    @abstractmethod
    def request_me_from_store(self, amt: int, where_to: 'WareHouse'):
        pass

    @abstractmethod
    def return_me_to_store(self, amt: int, where_from: 'WareHouse'):
        pass

    @property
    @abstractmethod
    def my_location(self):
        pass


class OfficeEquipment(DistributableWare):
    def __init__(self, name, price, make, model, store: 'WareHouse'):
        self.store = store
        self.name = name
        self.positions = {self.store.name: 1}
        self.price = price
        self.make = make
        self.model = model
        self.return_me_to_store(0)

    def __str__(self):
        params = ''
        for key in self.__dict__:
            if key == 'store':
                params = f"{params}{key} : {self.__dict__[key].name} \n"
            else:
                f"{params}{key} : {self.__dict__[key]} \n"
        return params

    def return_me_to_store(self, amt: int, where_from: 'WareHouse' = None):
        if where_from is not None:
            self.positions[where_from.name] -= amt
        self.positions[self.store.name] += amt  # если вернулось больше чем туда ушло - ну что ж, значит их
        return self.positions[self.store.name]  # там делают

    def request_me_from_store(self, amt: int, where_to: 'WareHouse'):
        in_stock = self.positions[self.store.name]
        if amt <= in_stock:
            self.positions[where_to.name] = amt
            self.positions[self.store.name] -= amt
            return self.positions[self.store.name]
        else:
            return -1

    def my_location(self):
        return self.positions


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


if __name__ == '__main__':
    stock = WareHouse('База')
    office = WareHouse('Нижнее Гадюкино')
    # начнём  с того, что положим на склад некоторое количество добра
    items = [Printer(10000, 'Canon', 'CX50', True, stock),
             Scanner(5000, 'Asus', 'MadeSimple', True, stock),
             CopyMachine(50000, 'Samsung', 'S1000', True, stock),
             CopyMachine(50000, 'Samsung', 'S1000', True, office),
             ]
    items[1].return_me_to_store(2)  # доложим ещё немного добра, которое у нас уже есть - пару сканеров, например
    print(StoreHelper.list(items, stock))
    # предположим, у нас есть филиал Нижнее Гадюкино, в который срочно надо сканеры и копиры, но копиров мало
    print("===поставляем два копира за 50 тыр и два сканера за 5 тыр в Нижнее Гадюкино:")
    shipment_list = (items[1], items[2])
    for el in shipment_list:
        if el.request_me_from_store(2, office) == -1:
            print(f'=Не удалось поставить {el.name} {el.make} {el.model} в {office.name}')
        else:
            print(f'=Отгрузили {el.name} {el.make} {el.model} в {office.name}')
    print(f'====Состояние склада:')
    print(StoreHelper.list(items, office))
    # один сканер в Гадюкино сломался, и нам его вернули.
    print("==Гадюкинцы вернули один сканер")
    shipment_list[0].return_me_to_store(1, office)
    print('====Состояние склада:')
    print(StoreHelper.list(items, stock))
    print("==А где это у нас сканеры все?")
    print(shipment_list[0].my_location())
    print("==Надо один принтер списать")
    recycle_bin = WareHouse('Списанное оборудование')
    items[0].request_me_from_store(1, recycle_bin)
    print(StoreHelper.list(items, recycle_bin))
    print(StoreHelper.list(items, stock))
