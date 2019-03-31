from collections import Counter

s = "happy three friends"

print(f'Исходная строка  - {s}')


class Node:
    def __init__(self,left = None,right = None):
        self.left = left
        self.right = right
    def __repr__(self):
        return f'Левая сторона [{self.left}] Правая сторона [{self.right}]'
    def children(self):
        return self.left, self.right

def make_haffman_tree(node, code=''):

    if type(node) is str:
        return {
            node:code
        }

    l,r = node.children()

    result = {}

    result.update(make_haffman_tree(l, code + '0')) #распихиваем 0 и 1
    result.update(make_haffman_tree(r, code + '1'))
    return result

count_s = Counter(s)

tree = count_s.items()

while len(tree) >1: # строим дерево матрешкой, порядковую зависимось эл-тов, каждый раз срезая суммированный конец
    tree = sorted(tree,reverse = True, key = lambda x:x[1])
    print(tree)
    char1,count1 = tree[-1]
    char2,count2 = tree[-2]
    tree = tree[:-2]
    tree.append(
        (Node(char1,char2), count1+count2)
    )

code_table = make_haffman_tree(tree[0][0])
print(f'\nСформированная таблица кодов символов - {code_table}')
coded = []

for char in s:
    coded.append(code_table[char])

print('Закодированная строка: %s'%''.join(coded))