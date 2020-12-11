"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
from random import sample
integers = [f'{el}' for el in sample(list(range(1, 101)),10)]
try:
    with open("numbers.txt", "w") as fhandle:
        fhandle.writelines(" ".join(integers))
    with open("numbers.txt", "r") as fhandl:
        select = fhandl.readline()
        result = sum([int(el) for el in select.split(' ')])
    print(f'Выборка - {select}, Сумма выборки - {result}')
except Exception as err:
    print(err)
