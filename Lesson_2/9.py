"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.
"""

max_cl = 0
sum_cl = 0

n = int(input("Введите количество сравниваемых чисел"))
for i in range(n):
    cl = int(input(f"Введите {i+1} число"))
    summ= 0
    temp_cl=cl
    while temp_cl > 0 :
        summ += temp_cl%10
        temp_cl= temp_cl//10
    if summ > sum_cl:
        sum_cl = summ
        max_cl = cl

print(f'Число {max_cl} имеет максимальную сумму цифр: {sum_cl}')