import hashlib


def sub_s_count(s):

    sub_s = set()

    for i in range(len(s)-1):
        for j in range(len(s), i, -1):
            sub_s.add(
                hashlib.sha1(s[i:j].encode('utf-8')).hexdigest())

    return sub_s


s = input('Введите строку из маленьких латинских букв: ')
print(f'Строка  - {s}')

for el in sub_s_count(s):
    print(el)

print(f'\nКоличество подстрок == {len(sub_s_count(s))}')