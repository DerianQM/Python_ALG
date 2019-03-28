"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
 который не рассматривался на уроках
"""


import random
from memory_profiler import profile
import timeit


def search(mass):
    left=[]
    right=[]
    for i in range(len(mass)):
        for j in range(len(mass)):
            if mass[i] > mass[j]:
                left.append(mass[j])
            if mass[i] < mass[j]:
                right.append(mass[j])
            if mass[i] == mass[j] and mass.index(mass[i]) > mass.index(mass[j]):
                left.append(mass[j])
            if mass[i] == mass[j] and mass.index(mass[i]) < mass.index(mass[j]):
                right.append(mass[j])
        #print(left)
        #print(right)
        #print('Длина левой',len(left))
        #print('длина правой',len(right))
        if len(left) == len(right):
            print(f"мединана {mass[i]}")
            break
        left.clear()
        right.clear()

@profile
def main(n):

    #mass = [random.randint(0, 100) for i in range(2 * n + 1)]
    mass = [34, 37, 53, 11, 14, 37, 64, 5, 74, 1, 36, 7, 19, 35, 13, 65, 68, 95, 50, 64, 26, 78, 81]
    print(f' массив - {mass}')
    search(mass)
    #print(f'элемент медианы -  {median(mass)}')
n = int(input("введите число, которое сченерирует массив"))

print(timeit.timeit('main(n)', setup = 'from __main__ import main,n', number =1))


'''
Через рекурсию за 10 проходов
n = 33
массив - [83, 70, 4, 26, 57, 31, 9, 98, 31, 86, 90, 19, 58, 26, 51, 94, 100, 92, 71, 60, 3, 48, 50, 47, 30, 30, 15, 78, 74, 76, 98, 97, 97, 61, 65, 28, 66, 57, 13, 35, 61, 87, 76, 16, 30, 88, 81, 73, 84, 58, 11, 42, 59, 20, 62, 76, 81, 82, 4, 83, 44, 87, 38, 81, 15, 75, 25]
элемент медианы -  60


Line #    Mem usage    Increment   Line Contents
================================================
    36     20.7 MiB     20.7 MiB   @profile
    37                             def main(n):
    38
    39     20.7 MiB      0.0 MiB       mass = [random.randint(0, 100) for i in range(2 * n + 1)]
    40
    41     20.7 MiB      0.0 MiB       print(f' массив - {mass}')
    42     20.7 MiB      0.0 MiB       print(f'элемент медианы -  {median(mass)}')


время - 0.08913925799999944




через sorted за 10 проходов
n = 33
массив - [43, 5, 49, 60, 2, 26, 31, 75, 17, 69, 65, 36, 5, 97, 67, 29, 26, 32, 36, 83, 15, 62, 90, 45, 95, 53, 55, 59, 89, 4, 26, 2, 50, 44, 70, 76, 47, 70, 12, 74, 26, 95, 33, 88, 35, 71, 51, 59, 37, 71, 52, 20, 77, 71, 39, 64, 96, 57, 75, 95, 94, 39, 67, 83, 27, 65, 18]
 медиана 53


Line #    Mem usage    Increment   Line Contents
================================================
    16     20.7 MiB     20.7 MiB   @ profile
    17                             def main(m):
    18     20.7 MiB      0.0 MiB       mass = [random.randint(0, 100) for i in range(2 * m + 1)]
    19
    20     20.7 MiB      0.0 MiB       print(f'массив - {mass}')
    21     20.7 MiB      0.0 MiB       print (f' медиана {median(mass)}')


время - 0.055866957000000106
'''

