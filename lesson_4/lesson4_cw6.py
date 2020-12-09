"""
Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый цикл не должен
быть бесконечным. Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл. Во втором
также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
"""
from itertools import count, cycle
from sys import argv


def iter1(start, fin):
    """
    итератор, генерирующий целые числа, начиная с указанного
    :return: список целых чисел начиная со start и до fin
    """
    result = []
    for i in count(start-1):
        if i == fin + 1:
            return result
        result.append(i)


def iter2(user_list, fin):
    """
    итератор, повторяющий элементы некоторого списка, определенного заранее
    :return: список, состоящий из элементов входящего списка, повторённых fin раз
    """
    result = []
    c = 0
    try:
        for i in cycle(user_list):
            if c == (fin)*len(user_list):
                return result
            result.append(i)
            c += 1
    except TypeError:
        return [user_list]


iteration = "Вводите аргументы правильно"
if int(argv[1]) == 1:
    try:
        arg_start = int(argv[2])
        arg_end = int(argv[3])
        iteration = iter1(arg_start, arg_end)
    except ValueError:
        print('Аргументы должны быть целыми числами!')
    except IndexError:
        print('Минимум три аргумента!')
elif int(argv[1]) == 2:
    try:
        arg_end = int(argv[2])
        arg_start_list = argv[3::]
        iteration = iter2(arg_start_list or ["No list defined"], arg_end or 1)
    except IndexError:
        print('Минимум три аргумента!')
else:
    print("lesson4_cw6.py [1 <начало отсчета> <конец последовательности>|2 <множество, "
          "через пробел> <кол-во повторений>] ")

print(iteration)
