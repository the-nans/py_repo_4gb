"""
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
import sys
try:
    with open("test.txt", "w") as f_handle:
        while 1:
            str = input('? \n')
            f_handle.write(f'{str} \n')
            if str == '':
                break
except Exception as err:
    print(err)

