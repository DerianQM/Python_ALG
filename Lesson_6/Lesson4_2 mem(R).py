import cProfile

from memory_profiler import profile

@profile
def main():
    s = int(input('введите позицию i-го элемента..., условимся, что отсчет начнем с 1-цы'))
    a=[]
    b=[]
    start = 0
    step = 20 # для динамики можно задать позицию шага с клавиатуры
    #step = int(input('введите предполагаемое количество элементов последовательности...'))
    check =0
    fl=0
    while fl == 0 :
        while start<step:
            a.append(start)
            start+=1
        if a[1]!=0:
            a[1]=0




        m =2
        while m <len(a) :
            if a[m]!=0:
                j=m*2
                while j < len(a):
                    a[j] = 0
                    j = j + m

            m+=1




        while check < len(a):
            if a[check]!=0:
                b.append(a[check])
                if len(b)+1 > s:
                    fl+=1
                    break
            check+=1

        start=step
        step = step+start




    print(b)

    print(f'{s}-й элемент равен {b[len(b)-1]}')

if __name__ == '__main__':
    main()