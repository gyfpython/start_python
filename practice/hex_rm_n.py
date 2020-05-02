def remove_n(num: hex, size: int):
    if int(num) < 2 ** size:
        print(hex(2 ** size))
    elif int(num) == 2 ** size:
        print(hex(num))
    else:
        temp_num = (num >> size) << size
        if num == temp_num:
            print(hex(num))
        else:
            num = num >> size
            print(hex((num + 1) << size))


remove_n(0xa, 4)
