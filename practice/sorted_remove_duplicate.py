'''
sorted and remove duplicate str in string
'''


def string_rm_duplicate(str1: str):
    return sorted(set(list(str1)))


print(''.join(string_rm_duplicate('abcddag')))
