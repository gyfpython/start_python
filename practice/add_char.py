"""
if string length < 8
add 0 to length 8
if string length >= 8
split 8 to all
string.ljust(num, char): add char until length of string is num
"""


def split_eight(string: str):
    k = len(string)//8
    result_list = []
    for i in range(k):
        result_list.append(string[i*8: (i+1)*8])
    if len(string) % 8 > 0:
        result_list.append(string[-(len(string) % 8):].ljust(8, '0'))
    return result_list


print(split_eight('qwuiereysjdkfh'))
