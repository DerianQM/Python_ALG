"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. По возможности доработайте алгоритм (сделайте его умнее).
"""




import random
import timeit
from memory_profiler import profile


def sorted(mass):
    flag = 0
    for i in range(len(mass)):
        for j in range(len(mass)-1):
            if mass[j] < mass[j+1]:
                mass[j], mass[j+1] = mass[j+1], mass[j]
                flag = 1
        if flag == 0 :
            break
        else:
            flag = 0
    return mass



@profile
def main(n):
    mass = [random.randint(-100, 100) for i in range(n)]
    print(f'Изначальный массив {mass}')
    print(f'Отсортированный массив - {sorted(mass)}')

n = int(input('Задайте длину массива'))
print(timeit.timeit('main(n)', setup = 'from __main__ import main,n', number =10))

# время сортировки за 10 проходов - 0.24866938299999974

'''
при значении 1000 эл-тов

Line #    Mem usage    Increment   Line Contents
================================================
    15     20.7 MiB     20.7 MiB   @profile
    16                             def main(n):
    17     20.7 MiB      0.0 MiB       mass = [random.randint(-100, 100) for i in range(n)]
    18     20.7 MiB      0.0 MiB       print(f'Изначальный массив {mass}')
    19     20.8 MiB      0.1 MiB       print(f'Отсортированный массив - {sorted(mass)}')
'''
'''
при значении 1700 эл-тов

Line #    Mem usage    Increment   Line Contents
================================================
    15     20.7 MiB     20.7 MiB   @profile
    16                             def main(n):
    17     20.7 MiB      0.0 MiB       mass = [random.randint(-100, 100) for i in range(n)]
    18     20.7 MiB      0.0 MiB       print(f'Изначальный массив {mass}')
    19     20.8 MiB      0.1 MiB       print(f'Отсортированный массив - {sorted(mass)}')

'''
# время сортировки за 1 проход при количестве эл-тов 1700 - 4.720054449999999, при 10 проходах Cprofile умирает

# время, после установки флага - 3.4892845
