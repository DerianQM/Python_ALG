"""
8.	Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и
записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
"""


# сделал немного динамичнее , чем в задаче вводом размера матрицы
n = int(input('Введите количество cтрок и матрице'))
m = int(input('Введите количество элементов в строке'))

def matrixprint (matrix):
    for row in matrix:
        for elem in row:
            print(elem, end=' ')
        print()



matrix = []

# создадим для наглядности
for i in range(n):
    matrix.append([])
    for j in range(m):
        matrix[i].append(0)

matrixprint (matrix)
# заполним кроме последнего элемента и в этом же цикле рассчитаем и запишем последний элемент
summ = 0

for i in range(n):
    for j in range(m-1):
        matrix[i][j] = int(input(f'Введите Элемент {i+1} {j+1} - '))
        summ += matrix[i][j]
    matrix[i][m-1] = summ
    summ = 0

matrixprint (matrix)
