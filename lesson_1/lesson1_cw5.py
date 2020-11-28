"""
Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки).
Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки
(соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
"""
credit = float(input('Введите значение выручки: '))
debit = float(input('Введите значение издержек: '))
if credit < debit:
    print('Какое убыточное предприятие!')
elif credit == debit:
    print("Вышли в ноль - уже неплохо!")
else:
    print(f'Рентабельность за период - {credit / (credit - debit):.2f}')
    workers = int(input('Введите количество сотрудников'))
    print(f'Прибыль на одного сотрудника - {(credit - debit)/workers:.2f}')