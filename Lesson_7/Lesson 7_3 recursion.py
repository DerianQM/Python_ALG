"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
 который не рассматривался на уроках
"""

import random
import timeit
from memory_profiler import profile



def median(mass, rand_el=random.choice):
    if len(mass) % 2 == 1:
        return select(mass, len(mass) / 2, rand_el)
    else:
        return (select(mass, len(mass) / 2 - 1, rand_el) +
                      select(mass, len(mass) / 2, rand_el))/2


def select(mass, len_index, rand_el):

    if len(mass) == 1:
        return mass[0]
    M = rand_el(mass)

    left = [i for i in mass if i < M]
    right = [i for i in mass if i > M]
    middle = [i for i in mass if i == M]

    if len_index < len(left):
        return select(left, len_index, rand_el)
    elif len_index < len(left) + len( middle):
        return middle[0]
    else:
        return select(right, len_index - len(left) - len(middle), rand_el)

n = int(input("введите число, которое сгенерирует массив"))

@profile
def main(n):

    mass = [random.randint(0, 100) for i in range(2 * n + 1)]

    print(f' массив - {mass}')
    print(f'элемент медианы -  {median(mass)}')

print(timeit.timeit('main(n)', setup = 'from __main__ import main,n', number =10))