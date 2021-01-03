"""
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""


def collect_user_data(name, surname, birthdate="", town="", email="", phone=""):
    """
    Функция получает значения имени, фамилии, даты и места рождения, email и телефона пользователя и
    выводит их одной строкой

    :param name:  string
    :param surname:  string
    :param birthdate: string
    :param town: string
    :param email: string
    :param phone: string
    :return: string
    """

    return f'{name} {surname} {birthdate} {town} {email} {phone}'


print(collect_user_data('Anya', 'Ovsienko', '15.04.1987', 'Moscow', 'venickovna@mail.ru', '89105653322'))
