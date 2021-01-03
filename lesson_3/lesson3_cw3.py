"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших
двух аргументов.
"""
def my_func(a, b, c):
    """
    Функция принимает на вход  три аргумента и возвращает сумму двух наибольших. Можно числа, строки, итераблы.
    :param a: basic or iterable
    :param b: basic or iterable
    :param c: basic or iterable
    :return: basic or iterable
    """
    values = [a,b,c]
    return sorted(values)[-1] + sorted(values)[-2]

print(my_func((1,2), (2,3), (3,4)))
print(my_func(1,2,3))
print(my_func('sefw','werD','afre'))