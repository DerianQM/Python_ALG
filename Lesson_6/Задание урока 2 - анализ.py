from memory_profiler import profile

@profile

def main():
    n = int(input("Введите число"))
    m = 0
    print(f"Ваше число - {n}")
    while n>0:
        m = m*10 + n%10
        n = n//10
    print(f"перевернутое {m}")

if __name__ =='__main__':
    main()



'''
Ваше число - 5678984
перевернутое 4898765
Filename: C:\Users\kor_g\OneDrive\Рабочий стол\Задание урока 2 - анализ.py

Line #    Mem usage    Increment   Line Contents
================================================
     3     19.6 MiB     19.6 MiB   @profile
     4
     5                             def main():
     6     19.6 MiB      0.0 MiB       n = int(input("Введите число"))
     7     19.6 MiB      0.0 MiB       m = 0
     8     19.6 MiB      0.0 MiB       print(f"Ваше число - {n}")
     9     19.6 MiB      0.0 MiB       while n>0:
    10     19.6 MiB      0.0 MiB           m = m*10 + n%10
    11     19.6 MiB      0.0 MiB           n = n//10
    12     19.6 MiB      0.0 MiB       print(f"перевернутое {m}")
'''
