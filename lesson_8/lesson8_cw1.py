"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

"""


class BadDateException(Exception):
    def __init__(self, text):
        self.txt = text


class Date:
    long_months = [1, 3, 5, 7, 8, 10, 12]
    short_months = [4, 6, 9, 11]
    february = [28]
    february_leap = [29]

    def __init__(self, day):
        self.day = day

    @staticmethod
    def date_validate(day: str):
        li = Date.date_to_number(day)

        leapflag = 1 if li[2] % 4 == 0 else 0

        if li[1] in Date.long_months and li[0] > 31 or li[1] in Date.short_months and li[0] > 30:
            raise BadDateException("Wrong day of the month!")
        if leapflag and li[0] > 29 or li[0] > 28:
            raise BadDateException("Too big day for February")
        if not (0 < li[1] < 13):
            raise Exception("Invalid month")
        return True

    @classmethod
    def date_to_number(cls, day: str):
        li = day.split('-')
        li_int = [int(el) for el in day.split('-')]
        return li_int


if __name__ == "__main__":
    Date.date_validate('11-12-2020')
    Date.date_validate('5-12-2020')
    Date.date_validate('11-22-2020')
    Date.date_validate('32-02-2020')
    Date.date_validate('---')
