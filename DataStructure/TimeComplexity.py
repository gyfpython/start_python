# 常见渐进时间复杂度 O(n), O(logn), O(1), O(n2)

def eat1(n: int):
    # 时间复杂度O(n)
    for i in range(n):
        print("wait 1S")
        print("eat 1cm")


def eat2(n: int):
    # 时间复杂度 O(logn)
    while n > 1:
        print("wait 1S")
        print("eat half")
        n //= 2


def eat3(n: int):
    # 时间复杂度 O(1)
    print("wait 1S")
    print("eat all")


def eat4(n: int):
    # 时间复杂度 O(n2)
    for i in range(n):
        for j in range(i):
            print("wait 1S")
        print("eat 1cm")


if __name__ == "__main__":
    eat4(10)
    eat3(10)
    eat2(10)
    eat1(10)
