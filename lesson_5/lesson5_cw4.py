"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться
в новый текстовый файл.
"""

num_dict = {
    "One" : "Один",
    "Two" : "Два",
    "Three" : "Три",
    "Four" : "Четыре"
}
ru_lines = []
try:
    with open("123.txt", "r") as fhandle:
        for lines in fhandle.readlines():
            l = f'{num_dict[lines.split(" — ")[0]]} — {lines.split(" — ")[1]}'
            print(l)
            ru_lines.append(l)
    with open("123-ru.txt", "w") as fhandle1:
        fhandle1.writelines(ru_lines)
except Exception as err:
    print(err)
