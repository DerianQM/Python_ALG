"""
6.	В одномерном массиве найти сумму элементов, находящихся
между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""
import random
A=[]
n = int(input("задайте длину массива"))
for i in range(n):
    A.append(random.randint(0,100))
print(f' массив - {A}')

step = abs(A.index(min(A)) - A.index(max(A)))

if step == 1:
    print('Элементы стоят рядом, складывать нечего')
else:
    s = min(A.index(min(A)), A.index(max(A))) + 1
    summ=0;
    for i in range (step-1):
        summ += A[s+i]
    print(f'сумма между {min(A)} и {max(A)} = {summ}')