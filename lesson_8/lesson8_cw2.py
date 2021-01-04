"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
 ситуацию и не завершиться с ошибкой.

"""
class MyShinyDivisionByZero(ZeroDivisionError):

    def __str__(self):
        return 'My shiny division by zero!'


def div(a, b):
    if not b:
        raise MyShinyDivisionByZero
    return a/b


if __name__ == "__main__":
    a = float(input('Введите делимое: '))
    b = float(input('Введите делитель: '))
    try:
        print(div(a, b))
    except MyShinyDivisionByZero as err:
        print(err)
        print('Давайте сегодня делитель будет 1')
        b = 1.0
        print(div(a, b))
