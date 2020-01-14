'''
lambda 表达式
“:” 左侧输入参数“,”分隔; 右侧返回值表达式
“:” 只能有一个表达式
'''

g = lambda x: x**2
print(g(2))

test = lambda x, y, z: (x+y)**z
print(test(1, 2, 3))

# lambda 可以用在list中
list1 = [lambda x: x**2, lambda x, y, z: (x+y)**z]
print(list1[0])
print(list1[0](2))
