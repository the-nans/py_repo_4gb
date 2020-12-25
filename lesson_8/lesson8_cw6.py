"""
Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, для
указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных
на уроках по ООП.

"""
from lesson8_cw5 import WareHouse, OfficeEquipment, Printer, Scanner, CopyMachine


class NotNumber(Exception):
    """
    Класс обработки ошибки ввода, когда введено нечисловое значение - буквы, пробел или перенос строки.
    """

    def __init__(self, expression):
        self.expression = expression

    def __str__(self):
        return f"Введено нечисловое значение {self.expression}!"


class StoreHelper:
    types_of_tech = "- Printer\n" \
                    "- Scanner\n" \
                    "- CopyMachine\n"

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

    @staticmethod
    def list_stores(store_list: 'list[WareHouse]'):
        """
        Выводит отформатированный, пронумерованный список складов, скрывает склад "Списанное оборудование"
        :param store_list:
        :return:
        """
        for whh in enumerate(store_list):
            if whh[0] != 0:
                wh = whh[1]
                print(f"{whh[0]}. {wh.name} {wh.shipment_address} {wh.phone} {wh.contact_person}")

    @staticmethod
    def list_tech(tech_list: 'list[OfficeEquipment]', wh: 'WareHouse'):
        """
        Выводит список оборудования в наличии на данном складе
        :param tech_list:
        :param wh:
        :return:
        """
        res_list = []
        for tll in enumerate(tech_list):
            tl = tll[1]
            locations_list = tl.positions.keys()
            if wh.name in locations_list and tl.positions[wh.name] > 0:
                print(f"id:{tll[0]}: {tl.name} {tl.make} {tl.model} {tl.price} - {tl.positions[tl.store.name]}")
                res_list.append(tll[0])
        return res_list  # набор uid-ов техники на данном складе

    @staticmethod
    def add_tech(type_tech: str, wh: 'WareHouse'):
        """
        Общается с пользователем, получая от него данные для добавления оборудования
        :param type_tech:
        :param wh:
        :return: экземпляр потомка OfficeEquipment
        """
        requests = {
            'Printer': 'Введите параметры оборудования в виде <Производитель> <Модель> <Стоимость><Цветной? -'
                       'Y/N>',
            'Scanner': 'Введите параметры оборудования в виде <Производитель> <Модель> <Стоимость><Работает с pdf? -'
                       'Y/N>',
            'CopyMachine': 'Введите параметры оборудования в виде <Производитель> <Модель> <Стоимость><Двусторонняя '
                           'печать - Y/N',
        }
        if type_tech in ['Printer', 'Scanner', 'CopyMachine']:
            make, model, price, b_param = StoreHelper.value_check(input(requests[type_tech]))
            res = eval(type_tech)(price, make, model, b_param, wh)
            return res

    @staticmethod
    def value_check(param):
        """
        Статический метод проверки параметров для создания экземпляра товара. Принимает пару ключ-значение
        :param param: может быть price, make, model, amt или что_угодно_ещё
        :return: price -> int, make, model -> str, что_угодно_ещё -> bool
        """
        make, model, price, b_param = param.split()
        price = StoreHelper.check_int(price)
        b_param = False if b_param in ['N', 'n', 'No', 'no', 'нет', 'Нет', 'н', 'Н'] else True
        return make, model, price, b_param

    @staticmethod
    def check_int(i):
        """
        Проверяет входной параметр на принадлежность к неотрицательным числам
        :param i:
        :return: positive float
        """
        if [x for x in i if x not in '1234567890.'] or i == '':
            raise NotNumber(i)
        else:
            return float(i)

    @staticmethod
    def choose_store(stores):
        """
        Общается с пользователем, предлагая ему выбрать склад из списка. Проверяет ввод пользователя на корректность
        :param stores:
        :return:
        """
        store_choice = f"{len(stores) + 1}"
        print("Выберите склад: ")
        StoreHelper.list_stores(stores)
        while StoreHelper.check_int(store_choice) > len(stores):
            store_choice = input('?: ')
        return int(store_choice)

    @staticmethod
    def choose_tech_type():
        """
        Общается с пользователем, пытаясь получить у него один из трёх имён классов офисной техники
        :return: строку
        """
        tech_to_add = ''
        while tech_to_add not in ['Printer', 'Scanner', 'CopyMachine']:
            tech_to_add = input(f"{StoreHelper.types_of_tech}\n?:")
        return tech_to_add

    @staticmethod
    def choose_tech(items, stores):
        """
        Общается с пользователем. Предлагает ему на выбор технику с данного склада, проверяет корректность ответа
        :param items:
        :param stores:
        :return: выбранный экземпляр класса техника
        """
        item_choice = len(items) + 1
        print("Выберите позицию: ")
        allowed_positions = StoreHelper.list_tech(items, stores)
        while StoreHelper.check_int(item_choice) not in allowed_positions:
            item_choice = input('?: ')
        return items[int(item_choice)]


if __name__ == '__main__':
    stores_list = [WareHouse('Списанное оборудование', 'Свалка под Дмитровом', 'Нет', 'Кузьмич'),
                   WareHouse('Головной Офис', 'Варшавское ш. 1', '8495-666-66-66', 'Михалыч'),
                   WareHouse('Деревня Гадюкино', 'Клинская обл., Гадюкино, д.2', '88653-66-66-66', 'Семёныч')]
    stock = stores_list[1]
    hardware_items = [Printer(10000, 'Canon', 'CX50', True, stock),
                      Scanner(5000, 'Asus', 'MadeSimple', True, stock),
                      CopyMachine(50000, 'Samsung', 'S1000', True, stock),
                      CopyMachine(50000, 'Samsung', 'S1000', True, stores_list[2])
                      ]
    next_store_choice = -1
    while True:
        print("Добавляем на склад новую позицию. Выберите склад или введите 0 для выхода")
        try:
            next_store_choice = StoreHelper.choose_store(stores_list)  # выбираем склад
            if next_store_choice == 0:
                break
            print("Введите один из типов оборудования:")
            hardware_to_add = StoreHelper.choose_tech_type()  # выбираем тип техники

            hardware_items.append(StoreHelper.add_tech(hardware_to_add, stores_list[int(next_store_choice)]))
        except NotNumber as err:
            print(err)
            print('Начнём с начала')
            continue

        StoreHelper.list_tech(hardware_items, stores_list[int(next_store_choice)])

        for wh1 in stores_list:
            print(wh1.name)
            c = 1
            StoreHelper.list_tech(hardware_items, wh1)
