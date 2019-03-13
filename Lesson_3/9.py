# 9.	Найти максимальный элемент среди минимальных элементов столбцов матрицы.
import random



n = int(input('Введите количество строк в матрице'))
m = int(input('Введите количество элементов в строке'))

def matrixprint (matrix):
    for row in matrix:
        for elem in row:
            print(elem, end=' ')
        print()


matrix = []
listmin = []
listmax = []

for i in range(n):
    matrix.append([])
    for j in range(m):
        matrix[i].append(random.randint(0,100))

matrixprint (matrix)


for j in range(m):
    for i in range (n):
        listmin.append(matrix[i][j])
    listmax.append(min(listmin))
    listmin.clear()

print(f"максимальный среди минимальных {max(listmax)}")