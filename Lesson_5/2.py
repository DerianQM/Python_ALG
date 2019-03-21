"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры
числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и
[‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

import collections

mass_s1=[]
mass_s2=[]
massumm=[]

d1 = collections.Counter()

def input_cl(mass,i):

    s1 =(input(f'Введите {i}е число'))
    for s in s1:
        if ord(s) in range(ord('a'),ord('f')+1) or ord(s) in range(ord('A'),ord('F')+1) or ord(s) in range(ord('0'),ord('9')+1) :
            mass.append(s.upper())

        else:
            print('Вы ввели не 16е число, повторите ввод')
            mass.clear()
            input_cl(mass,i)
            break
    return s1

def createCounter(d1):
    for i in range(0,16):
        if i<10:
            d1[i]=i
        else:
            d1[(chr(ord('A')+i-10))]=i


def retrans(mass,d1):
    sm=0
    for i in range(len(mass)):
        if mass[i].isnumeric():
            sm = sm + d1[int(mass[i])]*pow(16,(len(mass)-i-1))
        else:
            sm = sm + d1[mass[i]]*pow(16,(len(mass)-i-1))

    return sm


def revert(cl):
    mass=[]
    while cl > 16:
        mass.append(cl%16)
        cl= cl//16
    mass.append(cl%16)
    return mass

def view(massum,d1):
    result=[]
    for i in range(len(massumm)):
        result.append(list(d1.keys())[list(d1.values()).index(massumm[i])])
    result.reverse()
    return result

input_cl(mass_s1,1)
input_cl(mass_s2,2)


createCounter(d1)

part1 = retrans(mass_s1,d1)
part2 = retrans(mass_s2,d1)

massumm =revert(part1+part2)

print(f"результат сумммы числа {mass_s1} и числа {mass_s2} равен {view(massumm,d1)}")
massumm.clear()

massumm = revert(part1*part2)
print(f"результат умножения числа {mass_s1} и числа {mass_s2} равен {view(massumm,d1)}")