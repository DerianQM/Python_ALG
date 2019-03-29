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
            if mass[i] == mass[j] and i > j:
                left.append(mass[j])
            if mass[i] == mass[j] and i < j:
                right.append(mass[j])

        if len(left) == len(right):
            print(f"мединана {mass[i]}")
            break
        left.clear()
        right.clear()

@profile
def main(n):

    mass = [random.randint(0, 100) for i in range(2 * n + 1)]
    #mass = [55, 89, 7, 70, 38, 76, 26, 84, 32, 96, 22, 71, 60, 70, 73]
    print(f' массив - {mass}')
    search(mass)

n = int(input("введите число, которое сченерирует массив"))

print(timeit.timeit('main(n)', setup = 'from __main__ import main,n', number =10))


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


время за 10 проходов - 0.08913925799999944




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


время за 10 проходов - 0.055866957000000106
'''

'''
через шейкерную сортировку за 10 проходов

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


'''
через свою реализацию через цикл за 10 проходов

массив - [15, 88, 69, 71, 35, 36, 99, 29, 10, 67, 80, 69, 27, 48, 56, 50, 77, 41, 21, 12, 82, 66, 10]
мединана 50


Line #    Mem usage    Increment   Line Contents
================================================
    26     20.5 MiB     20.5 MiB   @profile
    27                             def main(n):
    28
    29     20.5 MiB      0.0 MiB       mass = [random.randint(0, 100) for i in range(2 * n + 1)]
    30                                 #mass = [55, 89, 7, 70, 38, 76, 26, 84, 32, 96, 22, 71, 60, 70, 73]
    31     20.5 MiB      0.0 MiB       print(f' массив - {mass}')
    32     20.5 MiB      0.0 MiB       search(mass)


время за 10 проходов - 0.08048060299999982

'''