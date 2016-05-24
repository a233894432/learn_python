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
