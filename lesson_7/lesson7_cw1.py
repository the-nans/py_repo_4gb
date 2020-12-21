"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
(двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.

"""

"""
это... складывать матрицы разного размера нельзя. Но конкретно в этой программе можно, с допущением, что "ноль" и 
"ничего" это одно и то же. Я понимаю, что в математике это не всегда так, но конкретно тут - так. Наслаждайтесь. 
"""

class Matrix:
    def __init__(self, matrix_rows: list):

        def cut_trailing_zeroes(row):
            """
            отрывает последние нули из строк, например
            :param row: 0,1,2,3,0,0
            :return: 0,1,2,3
            """
            while len(row) > 0:
                if row[len(row) - 1] == 0:
                    row.pop(len(row) - 1)
                else:
                    break
            return row

        self.matrix_lines = matrix_rows.copy()      # копируем значения аргумента
        for line in self.matrix_lines:
                cut_trailing_zeroes(line)
        self.start_max_row = self.matrix_lines[0]
        for matrix in self.matrix_lines:
            self.start_max_row = matrix if len(matrix) > len(self.start_max_row) else self.start_max_row
        self.start_max_col = len(self.matrix_lines)

    def __row_add(self, row1, row2):
        """
        сложение двух строк матрицы. Если одна строка длиннее другой - обрабатывается исключение IndexError
        :param row1: список чисел
        :param row2: список чисел
        :return: список элементов строки результата суммы
        """
        row3 = []
        if len(row1) < len(row2):
            row2, row1 = row1, row2
        for el in row1:
            try:
                row3.append(el + row2[row1.index(el)])
            except IndexError:
                row3.append(el)
        return row3

    def __columns_equalize(self, zeroes_amount):
        """
        Заполняет нулями пустые ячейки матрицы
        :return: None
        """
        for line in self.matrix_lines:
            j = 1
            len_line = len(line)                # запоминаем, какой длины у нас всё было в начале
            while j <= zeroes_amount - len_line:
                line.append(0)
                j += 1

    def __rows_equalize(self, rows_amount):
        """
        Добавляет в матрицу строки, заполненные нулями
        :param rows_amount:
        :return: None
        """
        i = 0
        while i < rows_amount:
            t = [0 for x in range(0, len(self.start_max_row))]
            self.matrix_lines.append(t)
            i += 1


    def __zero_rows_cut(self):
        """
        отрезает строки, полностью заполненные нулями
        :return: None
        """
        zero_lines_list = list(map(lambda matrix_to_check: 1 if [x for x in matrix_to_check if x > 0] else 0,
                                   self.matrix_lines))
        i = self.start_max_col - 1
        while i > 0:
            if zero_lines_list[i] == 0:
                self.matrix_lines = self.matrix_lines[:-1:]
                i -= 1
            else:
                break

    def __beautify(self):
        """
        вырезает из матрицы мусор при подготовке к выводу на печать
        :return: матрицу без всего лишнего. Исходная матрица не страдает
        """
        __beau = self.__copy__()
        __beau.__columns_equalize(len(__beau.start_max_row))
        __beau.__zero_rows_cut()

        return __beau

    def __copy__(self):
        return Matrix(self.matrix_lines)

    def __add__(self, other):
        max_width = max(len(self.start_max_row), len(other.start_max_row))
        max_height = max(self.start_max_col, other.start_max_col)

        self.__columns_equalize(max_width)
        other.__columns_equalize(max_width)

        self.__rows_equalize(max_height - self.start_max_col)
        other.__rows_equalize(max_height - other.start_max_col)

        m1 = self.matrix_lines.copy()
        m2 = other.matrix_lines.copy()
        j = 0
        temp_matrix = []
        while j < max_height:
            temp_row = []
            i = 0
            while i < max_width:
                temp_row.append(m1[j][i] + m2[j][i])
                i += 1
            temp_matrix.append(temp_row)

            j += 1
        return Matrix(temp_matrix)

    def __str__(self):
        to_print = self.__beautify()
        temp_str = ""
        for line in to_print.matrix_lines:
            for item in line:
                temp_str = f"{temp_str} {item:5}"
            temp_str = f"{temp_str} \n"

        return temp_str

if __name__ == "__main__":
    matr1 = Matrix([[-5, -6], [1,2,3,4,5], []])
    matr2 = Matrix([[5, 6], [1,2,3,4,-5], [], [1,1,1,1,1], []])

    print(f"{matr1} + \n{matr1} + \n{matr2} = \n")
    print(matr1 + matr1 + matr2)