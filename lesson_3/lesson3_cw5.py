"""
Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться
сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь
введенных чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ,
выполнение программы завершается. Если специальный символ введен после нескольких чисел, то вначале нужно добавить
сумму этих чисел к полученной ранее сумме и после этого завершить программу.
"""
summa = 0
flag = ''
while flag != 'b':
    try:
        user_input = input('? \n')
        str = user_input.split(' b')[0].split(" ")
        flag = 'b' if 'b' in user_input else ''
    except ValueError as err:
        print(err)
        break
    try:
        summa = sum( list(map(lambda x: float(x), str))) + summa
    except ValueError as err:
        print(err)
    except AttributeError as err:
        print(err)
print(summa)
