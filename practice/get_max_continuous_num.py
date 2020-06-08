"""
get max continuous number of a given number list
"""


def max_continuous_num(input_list: list):
    if not input_list:
        max_len = 0
        return max_len
    max_len = 1
    tem_list = list(set(input_list))
    tem_list1 = []
    tem_list1.append(tem_list[0])
    for num in range(1, len(tem_list)):
        if tem_list[num] == tem_list[num-1] + 1:
            tem_list1.append(tem_list[num])
        else:
            if len(tem_list1) >= max_len:
                max_len = len(tem_list1)
            tem_list1 = []
            tem_list1.append(tem_list[num])
    if len(tem_list1) >= max_len:
        max_len = len(tem_list1)
    return max_len


test_list = [2, 3, 9, 6, 7, 1, 8, 0, 4, 11, 12, 13, 14, 15, 16]
print(max_continuous_num(test_list))
