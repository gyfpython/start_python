# 常见空间复杂度 O(1), O(n), O(n2)

def fun1(n: int):
    # 空间复杂度 O(1)
    i = 3
    # do sth


def fun2(n: int):
    # 空间复杂度 O(n)
    array = [[0] * n]
    # do sth


def fun3(n: int):
    # 空间复杂度 O(n2)
    matrix = [[0] * n] * n
    # do sth


if __name__ == "__main__":
    fun3(10)
    fun2(10)
    fun1(10)

