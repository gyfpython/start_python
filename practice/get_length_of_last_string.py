'''
input a string, return length of last word
'''


def get_length(string: str):
    temp_list = string.split()
    return len(temp_list[-1])


print(get_length('hello world'))
