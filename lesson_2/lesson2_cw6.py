"""
*Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит
информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения). Структуру нужно сформировать программно,
т.е. запрашивать все данные у пользователя.
Пример готовой структуры:
[
    (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
    (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
    (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например
название, а значение — список значений-характеристик, например список названий товаров.
Пример:
{
    “название”: [“компьютер”, “принтер”, “сканер”],
    “цена”: [20000, 6000, 2000],
    “количество”: [5, 2, 7],
    “ед”: [“шт.”]
}

"""
# сделаем исходно склад непустым, чтобы не наполнять с нуля
store_list = [(1, {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'eд': 'шт.'}),
              (2, {'название': 'принтер', 'цена': 6000, 'количество': 2, 'eд': 'шт.'}),
              (3, {'название': 'сканер', 'цена': 2000, 'количество': 7, 'eд': 'шт.'})]

# набор имеющихся наименований, чтобы пользователь не вводил дублей.
names_set = set()
for el in store_list:
    names_set.add(el[1].get('название'))

i = len(store_list)+1  # индекс последнего товара на складе

print('Сейчас в каталоге: ')
for store_item in store_list:
    print(store_item)


add = ''    # Хотим ли мы добавить ещё товар


while add != 'n':
    if add.upper() == 'Y':
        # добавление товара на склад
        item_name = input('Введите название товара: ')
        if item_name in names_set:
            print('Такой товар уже есть на складе. Выходим. ')
            continue
        else:
            names_set.add(item_name)
        item_price = int(input('Введите цену товара: '))
        item_qty = int(input('Введите количество товара: '))
        item_measure = input('Введите единицу измерения товара: ')

        store_list.append((i, {'название': item_name, 'цена': item_price, 'количество': item_qty, 'eд': item_measure}))
        i += 1
    elif add == 'n':
        break

    add = input('Добавить ещё товар в каталог? [Введите Y или n]') or 'Y'
# анализируем содержимое склада, с учётом дополнений пользователя
analytics = {}
temp_set = set()
for key in store_list[0][1].keys():     # множество значений параметров берём из первого товара на складе
    for el in store_list:
        temp_set.add(el[1].get(key))    # наполняем временное множество значениями очередного параметра
    analytics.update({key: list(temp_set)})     # множество становится списком и ключуется очередным параметром товара
    temp_set.clear()    # чистим временное множество. На список, сделанный из него, это не влияет
print('Разнообразие параметров в каталоге: ')
for characteristic, value in analytics.items():
    print(f'{characteristic} : {value} ')


