# 数组在内存中顺序存储，对应python中list或者tuple；其中tuple不可变

def list_test():
    my_list = [3, 2, 4, 1, 5, 8, 7, 9, 0]
    print(my_list)
    my_list[3] = 10
    print(my_list)
    my_list.append(12)
    print(my_list)
    my_list.insert(5, 11)
    print(my_list)
    my_list.remove(2)
    print(my_list)


if __name__ == "__main__":
    list_test()
