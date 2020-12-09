"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. В расчете
необходимо использовать формулу: (выработка в часах*ставка в час) + премия. Для выполнения расчета для конкретных
значений необходимо запускать скрипт с параметрами.
"""
from sys import argv
script_name, working_hours, hourly_payment, bounty = argv

try:
    print(f'{working_hours} {hourly_payment} {bounty}')
    print('%.2f'%(float(working_hours)*float(hourly_payment) + float(bounty)))
except ValueError as err:
    print(err)
