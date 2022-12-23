"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса
(метод init()),
который должен принимать данные (список списков) для формирования матрицы.
[[], [], []]
Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в
привычном виде.

Далее реализовать перегрузку метода add() для реализации операции
сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.

Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.
"""


import copy


class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        el = ''
        for i in range(len(self.matrix)):
            el += '\t'.join(map(str, self.matrix[i])) + '\n'
        return el

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix):
            return "Такую матрицу нельзя сложить!"
        result = copy.deepcopy(self.matrix)
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                result[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return Matrix(result)


var_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
var_2 = [[11, 22, 33], [44, 55, 66], [77, 88, 99]]
m_1 = Matrix(var_1)
m_2 = Matrix(var_2)
print(m_1)
print(m_2)
my_sum = m_1 + m_2
print('Результат сложения матриц = ')
print(my_sum)
