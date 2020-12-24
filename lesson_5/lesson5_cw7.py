"""
Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать данные
о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1   ООО   10000   5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
убытки, в расчет средней прибыли ее не включать.

Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.

Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
"""
import random, json
# факультативно генерируем рынок
def companies_population():
    names = random.sample(["roga_i_kopyta", "Aeroflot", "OAO_RZD_Strelochnik", "Shurochkina_shushera",
                           "Lebedev_Studio"], 5)
    properties = random.sample(["ООО", "АО", "ТОО", "ДОУ", "ГП"], 5)
    profit = random.sample(list(range(10000, 50000)),5)
    loss = random.sample(list(range(9000, 55000)),5)
    company_dict = []
    totals = []
    for i in range(5):
        company_dict = [names[i], properties[i], str(profit[i]), str(loss[i])]
        totals.append(company_dict.copy())
    print(totals)
    with open("companies.txt", "w", encoding="utf-8") as fhandle:
        for el in totals:
            k = " ".join(el)
            fhandle.write(f'{k} \n')
companies_population()
# ================================================================
result = dict()
profitable = []
to_write = []
with open("companies.txt", 'r') as fhandle:
    for line in fhandle.read().splitlines():
        t = line.split(' ')
        result[t[0]]= int(t[2]) - int(t[3])
        if int(t[2]) - int(t[3]) > 0:
            profitable.append(int(t[2]) - int(t[3]))
    to_write.append(result)
    try:
        ap = round((sum(profitable) / round(len(profitable), 2)),2)
        print(f'average profit: {ap}')
        to_write.append({"average_profit": ap})
    except Exception as err:
        print(err)
        to_write.append({"average_profit": "no_profits"})
    print(result)
with open("companies_result.json", "w") as jhandle:
    json.dump(to_write, jhandle)
