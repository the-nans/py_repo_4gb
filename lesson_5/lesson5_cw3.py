"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов (не менее
10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить
подсчет средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32
"""
import random
# факультативно генерируем популяцию персонала
def neprogrammny_spisok_zarplat():
    names = random.sample(["Иван", "Анна", "Пётр", "Алексей", "Дмитрий", "Елена", "Татьяна", "Сергей", "Ольга",
                           "Николай"], 10)

    surnames = random.sample(["Кравчук", "Седых", "Котейко", "Шац", "Кац", "Гольдберг", "Виттенштайн", "Охапко",
                              "Кульман", "Штульберг"], 10)

    salaries_int = random.sample(list(range(10000, 50000)),10)
    salaries_float = random.sample([random.random().__round__(2) for i in range(10)], 10)
    salar = [el+el1 for el in salaries_float for el1 in salaries_int]

    salary_dict = {}
    salaries = []
    for i in range(10):
        salary_dict["Имя"] = names[i]
        salary_dict["Фамилия"] = surnames[i]
        salary_dict["Зарплата"] = salar[i]
        salaries.append(salary_dict.copy())

    with open("staff.txt", "w", encoding="utf-8") as fhandle:
        for el in salaries:
            for key, val in el.items():
                fhandle.write(f"{val},")
            fhandle.write('\n')


neprogrammny_spisok_zarplat()
# ================================================================

avg = 0
cnt = 0
try:
    with open("staff.txt") as fhandle:
        for lines in fhandle.readlines():
            if float(lines.split(",")[2]) < 20000 :
                print(lines)
            avg += float(lines.split(",")[2])
            cnt += 1
    print(f'Средняя зарплата: {(avg/cnt).__round__(2)}')
except Exception as err:
     print(err)
