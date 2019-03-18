# Задание 9 Урока 3
# Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random
import timeit

# изначальная функция вывода матрицы
'''
def matrixprint (matrix):  # - исходная функция
    for row in matrix:
        for elem in row:
            print(elem, end=' ')
        print()

'''
def matrixprint (matrix):  # - модифицированная функция
    for row in matrix:
        print(row)

def main(n,m):


    matrix = []
    listmin = []
    listmax = []

    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(random.randint(0,100))

   # matrixprint (matrix)    -  шаг 1й в анализе убираем отображение
   # print(matrix) - шаг 2й - выводим через стандартный print
    matrixprint (matrix) #  - шиг 3й модифицируем функцию

    for j in range(m):
        for i in range (n):
            listmin.append(matrix[i][j])
        listmax.append(min(listmin))
        listmin.clear()

    print(f"максимальный среди минимальных {max(listmax)}")

n = int(input('Введите количество строк в матрице'))
m = int(input('Введите количество элементов в строке'))

print(timeit.timeit('main(n,m)', setup = 'from __main__ import main,n,m', number =7))

'''
При размере матрицы 100*50 7 проходов

Время исходного кода — 0.30154630000000004
Время модифицированного кода — 0.05354290000000006
Время без вывода - 0.04016359999999963
'''
