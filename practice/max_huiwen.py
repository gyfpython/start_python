# 最长回文字

def get_max_huiwen(string: str):
    length, max_str, max_num = len(string), '', 0
    result_map = [[0 for i in range(length)] for j in range(length)]
    for k in range(length):
        for l in range(k + 1):
            if k - l <= 1:
                if string[k] == string[l]:
                    result_map[k][l] = 1
                    if k-l+1 > max_num:
                        max_str = string[l: k+1]
                        max_num = k-l+1
            else:
                if string[k] == string[l] and result_map[k - 1][l + 1] == 1:
                    result_map[k][l] = 1
                    if k - l + 1 > max_num:
                        max_str = string[l: k + 1]
                        max_num = k - l + 1
    print(max_str)


get_max_huiwen("lalalala123454321")