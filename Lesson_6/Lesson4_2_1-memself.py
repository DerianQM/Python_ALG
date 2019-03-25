from memory_profiler import profile

@profile
def main():
    n = int(input('введите i-е по счету простое число ...'))
    b = []
    m =2

    while len(b) < (n):
        i=2
        count = 0
        while i <(m+1) and count<=1:
            if m % i ==0:
                count+=1
            i+=1
        if count == 1:
            b.append(m)
        m+=1


    print(f'ряд равен = {b} условимся, что мы нумеруем ряд ,начиная с 1 ')

    print(f" {n} - элемент равен - {b[len(b)-1]}")

if __name__ == '__main__':
    main()
