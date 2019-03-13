# 4.	Определить, какое число в массиве встречается чаще всего.
import random

A=[]
n = int(input("задайте длину массива"))
for i in range(n):
    A.append(random.randint(1,100))
print(f' массив - {A}')
count = 1
cl=0
for i in range(len(A)):
    if A.count(A[i])>count:
        count = A.count(A[i])
        cl = A[i]
if count > 1:
    print(f'число {cl} встречается {count} раз(а)')
else:
    print('элементы в массиве уникальны')