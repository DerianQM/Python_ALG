#3.	В массиве случайных целых чисел поменять местами минимальный
# и максимальный элементы.
import random

A=[]
n = int(input("задайте длину массива"))
for i in range(n):
    A.append(random.randint(1,100))
print(f'исходный массив - {A}')
temp = min(A)
A[A.index(min(A))] = max(A)
A[A.index(max(A))] = temp
print(f'измененный массив - {A}')