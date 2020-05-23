import copy
a = ['a', 'b', 'c', [1, 2, 3]]
b = a
c = copy.copy(a)
d = copy.deepcopy(a)
a.append('d')
a[3].append(4)
c.append('e')

print(a)
print(b)
print(c)
print(d)
d.remove('c')
print(d)
d.insert(0, 'd')
print(d)
