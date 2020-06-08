"""
get all sorted of a string
"""


def all_str_sort(string: str):
    if not string:
        return None
    length = len(string)
    origin_list = [string[0]]
    for i in range(1, length):
        origin_list = insert_test(string[i], origin_list)
    print(len(origin_list), origin_list)


def insert_test(string1: str, test_list: list):
    temp_list = []
    for i in range(len(test_list)):
        for j in range(len(test_list[i])+1):
            str_list = list(test_list[i])
            str_list.insert(j, string1)
            result_str = ''.join(str_list)
            temp_list.append(result_str)
    return temp_list


test = 'qwert'
all_str_sort(test)
