# 2. Выполнить логические побитовые операции "И", "ИЛИ" и др.
# над числами 5 и 6. Выполнить
# над числом 5 побитовый сдвиг вправо и влево на два знака.

a = 5
b = 6
print(f"{a} имеет вид в битах {bin(a)}\n {b} имеет вид в битах {bin(b)}")
print(f"{a} И {b} = {a&b} в битах {bin(a&b)}")
print(f"{a} ИЛИ {b} = {a|b} в битах {bin(a|b)}")
print(f"Сдвиг {a} влево на 2 = {a<<2} в битах {bin(a<<2)}")
print(f"Сдвиг {a} вправо на 2 = {a>>2} в битах {bin(a>>2)}")