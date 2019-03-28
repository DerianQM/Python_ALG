"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

"""




import random
import timeit
from memory_profiler import profile

# разкоментить принты, чтобы наглядно посмотреть(брал алгоритм урока и пытался пошагово его разобрать)
def sorted_join (mass):
    if len(mass) > 1:
        c = len(mass) // 2
        left = mass[:c]
        right = mass[c:]

        #print(f"Левая часть {left}")
        #print(f"Правая часть {right}")

        sorted_join(left)
        sorted_join(right)

       #print("Перестали делить")
        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):

            #print(f'длина левой части - {len(left)} длина правой части - {len(right)}')
            if left[i] < right[j]:
                mass[k] = left[i]
                i += 1
                #print( f'массив -{mass}')
            else:
                mass[k] = right[j]
                j += 1
                #print( f'массив -{mass}')
            k += 1

        while i < len(left):
            mass[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            mass[k] = right[j]
            j += 1
            k += 1
        return mass

@profile
def main(n):

    mass = [random.randint(-100, 100) for i in range(n)]

    print(f'Изначальный массив {mass}')

    print(f'Отсортированный массив - {sorted_join(mass)}')


n = int(input('Задайте длину массива'))

print(timeit.timeit('main(n)', setup = 'from __main__ import main,n', number =10))



# Время выполнения за 10 проходов  - 0.03245310299999993 кол -во элементов 10

'''
результат при длине массива 10

Line #    Mem usage    Increment   Line Contents
================================================
    45     20.8 MiB     20.8 MiB   @profile
    46                             def main(n):
    47
    48     20.8 MiB      0.0 MiB       mass = [random.randint(-100, 100) for i in range(n)]
    49
    50     20.8 MiB      0.0 MiB       print(f'Изначальный массив {mass}')
    51
    52     20.8 MiB      0.0 MiB       print(f'Отсортированный массив - {sorted_join(mass)}')
'''
# Время выполнения за 10 проходов  - 12.638006205 кол -во элементов 10000
'''
результат при длине массива 10000

Line #    Mem usage    Increment   Line Contents
================================================
    45     21.4 MiB     21.4 MiB   @profile
    46                             def main(n):
    47
    48     21.4 MiB      0.0 MiB       mass = [random.randint(-100, 100) for i in range(n)]
    49
    50     20.9 MiB      0.0 MiB       print(f'Изначальный массив {mass}')
    51
    52     21.4 MiB      0.4 MiB       print(f'Отсортированный массив - {sorted_join(mass)}')
'''
#несмотря на вызов рекурсии, память они расходуют n/2 соответственон вызовов получается не так уж и много


