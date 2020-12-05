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
    try:
        return f'%.{precision}f'%(float(a) / float(b))
    except ZeroDivisionError as err:
        print('Division by zero')
        print(err)
        return None
    except ValueError as err:
        print(err)
        return None

print(div_a_b(5))
