def fun_a():
    print('a')


def fun_b():
    print('b')


def fun_c():
    print('c')


def switch_fun(selection: str):
    fun_map = {'a': fun_a,
               'b': fun_b,
               'c': fun_c}

    return fun_map[selection]()


if __name__ == '__main__':
    switch_fun('c')
    a = ['1', '2', '%', '4']
    print(a[:a.index('%') + 1])
    print(a[a.index('%') + 1:])
