import random


def get_random_int(num: int):
    return random.randint(0, num)


def random_append_list(list_test: list, number_dupl: int):
    i = 0
    str1 = ''
    while i < number_dupl:
        str1 = str1 + list_test[get_random_int(len(list_test)-1)]
        i = i + 1
    return str1


test = ['123', '345', '1233']
print(random_append_list(test, 5))
