t1 = 'a',
t2 = ('a')

print(type(t1))  # <class 'tuple'>
print(type(t2))  # <class 'str'>

# 列表和元组

s = 'abc'
t = [0, 1, 2]
zip(s, t)
for pair in zip(s, t):
    print(pair)

# 如果需要遍历一个序列的元素以及其索引号，您可以使用内建函数 enumerate ：
for index, element in enumerate('abc'):
    print(index, element)

# 字典和元组

d = {'a': 0, 'b': 1, 'c': 2}
t = d.items()
#  print(t) ==>  dict_items([('c', 2), ('a', 0), ('b', 1)])
from structshape import structshape

print(structshape(d))
