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

def median(mass):

    if len(mass) < 1:
            return mass
    if len(mass) % 2 == 1:
            return sorted(mass)[len(mass)//2]
    else:
            return sum(sorted(mass)[len(mass)//2-1:len(mass)//2+1])/2.0


@ profile
def main(m):
    mass = [random.randint(0, 100) for i in range(2 * m + 1)]
    #mass = [81, 45, 34, 61, 29, 25, 55, 60, 9, 9, 32, 66, 1, 8, 26, 81, 74, 89, 24, 41, 29, 92, 5, 76, 56, 88, 90, 8, 47, 81, 74, 32, 66, 1, 45, 52, 33, 24, 62, 52, 4, 62, 15, 91, 80, 3, 54, 10, 11, 92, 48, 73, 50, 21, 14, 50, 95, 19, 45, 90, 73, 88, 56, 44, 17, 95, 100]
    print(f'массив - {mass}')
    print (f' медиана {median(mass)}')

m = int(input("введите число, которое сченерирует массив"))
print(timeit.timeit('main(m)', setup = 'from __main__ import main,m', number =10))


# Время выполнения за 10 проходов  1.7306336590000004 -  кол -во элементов 1700

'''
Line #    Mem usage    Increment   Line Contents
================================================
    16     21.2 MiB     21.2 MiB   @ profile
    17                             def main(m):
    18     21.2 MiB      0.0 MiB       mass = [random.randint(0, 100) for i in range(2 * m + 1)]
    19
    20     21.2 MiB      0.0 MiB       print(f'массив - {mass}')
    21     21.2 MiB      0.0 MiB       print (f' медиана {median(mass)}')

'''
