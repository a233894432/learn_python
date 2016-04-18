from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
print(d)
c = defaultdict(set)
c['a'].add(1)
c['a'].add(2)
c['b'].add(4)
print(c)
print(c['a'])