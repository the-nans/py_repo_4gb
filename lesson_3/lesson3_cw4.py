"""
Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить
возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y). При решении задания
необходимо обойтись без встроенной функции возведения числа в степень
"""


def my_func(x, y=-1):
    """
    Функция возвращает первый аргумент, возведённый в степень, равную второму

    :param x: действительное положительное число
    :param y: целое отрицательное число
    :return: x в степени y
    """
    try:
        a = abs(int('%.0d'%y))
    except TypeError as err:
        return err
    pow = x     # копируем значение x в другую ячейку, для сохранности
    for i in range(1, a):
        x *= pow
    try:
        return 1/x
    except ZeroDivisionError as err:
        return err


# и через возведение в степень с помощью **


def my_func_simple(x, y=-1):
    """
    Функция возвращает первый аргумент, возведённый в степень, равную второму
    :param x: действительное положительное число
    :param y: целое отрицательное число
    :return: x в степени y
    """
    try:
        y = (-1)*abs(int('%.0d'%y))
        return x**y
    except ZeroDivisionError as err:
        print(err)
        return None
    except ValueError as err:
        print(err)
        return None
    except TypeError as err:
        print(err)
        return None


print(my_func(3, -4))
print(my_func_simple(3, -4))    # кстати, получается прикольное число
