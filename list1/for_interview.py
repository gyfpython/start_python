def string_rm_mutil(str1: str):
    return sorted(set(list(str1)))


print(''.join(string_rm_mutil('abcddag')))
