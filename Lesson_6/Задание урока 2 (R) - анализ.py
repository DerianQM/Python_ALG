from memory_profiler import profile

@profile
def recursion(n,m):
    if n == 0:
        print(f"перевернутое {m}")
    else:
        recursion(n//10,(m*10 + n%10))

#рекурсия
@profile
def main():
    n = int(input("Введите число"))
    print(f"Ваше число - {n}")
    recursion(n,0)


if __name__ =='__main__':
    main()


'''
Filename: C:\Users\kor_g\OneDrive\Рабочий стол\Задание урока 2 (R) - анализ.py

Line #    Mem usage    Increment   Line Contents
================================================
     3     19.9 MiB     19.8 MiB   @profile
     4                             def recursion(n,m):
     5     19.9 MiB      0.0 MiB       if n == 0:
     6     19.9 MiB      0.0 MiB           print(f"перевернутое {m}")
     7                                 else:
     8     19.9 MiB      0.0 MiB           recursion(n//10,(m*10 + n%10))


Filename: C:\Users\kor_g\OneDrive\Рабочий стол\Задание урока 2 (R) - анализ.py

Line #    Mem usage    Increment   Line Contents
================================================
    11     19.8 MiB     19.8 MiB   @profile
    12                             def main():
    13     19.8 MiB      0.0 MiB       n = int(input("Введите число"))
    14     19.8 MiB      0.0 MiB       print(f"Ваше число - {n}")
    15     19.9 MiB      0.1 MiB       recursion(n,0)
'''