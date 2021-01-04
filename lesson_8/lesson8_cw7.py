"""
Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку методов
сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа) и
выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
"""


class ComplexNumber:
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def __str__(self):
        b = ' + ' if self.b > 0 else ' - '
        b = f'{b}{abs(self.b)}' if abs(self.b) != 1 else f'{b}'
        if self.b != 0:
            return f"{self.a}{b}i"
        else:
            return f"{self.a}"

    def __add__(self, other):
        """
        z3 = a1 + a2 + (b1 + b2)i
        :param other: ComplexNumber
        :return: ComplexNumber
        """
        c = self.a + other.a
        d = self.b + other.b
        return ComplexNumber(c, d)

    def __mul__(self, other):
        """
        z3 = a1a2 - b1b2 + (a1b2 + a2b1)i
        :param other: ComplexNumber
        :return: ComplexNumber
        """
        c = self.a * other.a - self.b * other.b
        d = self.a * other.b + self.b * other.a

        return ComplexNumber(c,d)


z1 = ComplexNumber(2, 3)
z2 = ComplexNumber(-1, 0)
print(z1)
print(z2)
print(z2 + z1)
print(z2*z1)
