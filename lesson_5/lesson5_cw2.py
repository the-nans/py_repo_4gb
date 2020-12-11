"""
Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить
подсчет количества строк, количества слов в каждой строке.
"""


def count_line(file_handle):
    i = 1
    for line in file_handle:
        result = (i, len(line.strip().split(" "))) if line != '\n' else (i, 0)
        yield result
        i += 1
c = 0
try:
    with open("test.txt", "r") as f_handle:
        f = count_line(f_handle)
        while True:
            nextline = next(f)
            print(f'В строке {nextline[0]} - {nextline[1]} слов')
            c += 1
except StopIteration:
    print(f'Всего {c } строк')  # последний перенос строки ещё одной строкой не считаем
except FileNotFoundError as err:
    print(err)