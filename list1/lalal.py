#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'checkDivisibility' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY arr as parameter.
#

def get_all_str(string: str):
    if not string:
        return None
    length = len(string)
    origin_list = [string[0]]
    for i in range(1, length):
        origin_list = insert_test(string[i], origin_list)
    return origin_list

def insert_test(string1: str, test_list: list):
    temp_list = []
    for i in range(len(test_list)):
        for j in range(len(test_list[i])+1):
            str_list = list(test_list[i])
            str_list.insert(j, string1)
            result_str = ''.join(str_list)
            temp_list.append(result_str)
    return temp_list

def checkDivisibility(arr):
    # Write your code here
    result_list = []
    for n in arr:
        result = get_all_str(n)
        if not result:
            result_list.append('NO')
        else:
            for m in result:
                if int(m) % 8 == 0:
                    result_list.append('YES')
                    break
                if m == result[-1]:
                    result_list.append('NO')
    return result_list


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = input()
        arr.append(arr_item)

    result = checkDivisibility(arr)
    print(result)

    # fptr.write('\n'.join(result))
    # fptr.write('\n')
    #
    # fptr.close()
