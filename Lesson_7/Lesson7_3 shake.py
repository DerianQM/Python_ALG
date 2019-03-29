
import random
import timeit
from memory_profiler import profile




def sort(mass):


    left = 0
    right = len(mass) - 1

    while left <= right:
        for i in range(left, right, +1):
            if mass[i] > mass[i + 1]:
                mass[i], mass[i + 1] = mass[i + 1], mass[i]
        right -= 1

        for i in range(right, left, -1):
            if mass[i - 1] > mass[i]:
                mass[i], mass[i - 1] = mass[i - 1], mass[i]
        left += 1

    print(f'Отсортированный массив - {mass}')
    return(mass[len(mass)//2])

n = int(input("введите число, которое сгенерирует массив"))

@profile
def main(n):

    mass = [random.randint(0, 100) for i in range(2 * n + 1)]
    #mass = [75, 8, 98, 82, 20, 100, 75, 23, 73, 28, 42, 46, 96, 69, 22, 27, 64, 35, 20, 59, 23, 45, 1]
    print(f' массив - {mass}')
    print(f'элемент медианы -  {sort(mass)}')

print(timeit.timeit('main(n)', setup = 'from __main__ import main,n', number =10))


'''
массив - [64, 29, 54, 43, 68, 68, 2, 87, 78, 26, 13, 97, 34, 69, 6, 31, 48, 80, 63, 3, 55, 30, 89]
Отсортированный массив - [2, 3, 6, 13, 26, 29, 30, 31, 34, 43, 48, 54, 55, 63, 64, 68, 68, 69, 78, 80, 87, 89, 97]
элемент медианы -  54


Line #    Mem usage    Increment   Line Contents
================================================
    31     20.5 MiB     20.5 MiB   @profile
    32                             def main(n):
    33
    34     20.5 MiB      0.0 MiB       mass = [random.randint(0, 100) for i in range(2 * n + 1)]
    35                                 #mass = [75, 8, 98, 82, 20, 100, 75, 23, 73, 28, 42, 46, 96, 69, 22, 27, 64, 35, 20, 59, 23, 45, 1]
    36     20.5 MiB      0.0 MiB       print(f' массив - {mass}')
    37     20.5 MiB      0.0 MiB       print(f'элемент медианы -  {sort(mass)}')


время за 10 проходов - 0.03849951299999965
'''