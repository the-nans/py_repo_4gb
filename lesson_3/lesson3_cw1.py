"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать
у пользователя, предусмотреть обработку ситуации деления на ноль.

"""


def div_a_b(precision = 3):
    """
    Функция выполняет деление двух чисел, возвращает результат заданной точности с плавающей точкой

    :param precision: int
    :return: float
    """
    a = input('Enter float a: ')
    b = input('Enter float b: ')
    return f'%.{precision}f'%(float(a) / float(b))


try:
    print(div_a_b(5))
except ZeroDivisionError as err:
    print(err)
except ValueError as err1:
    print(err1)