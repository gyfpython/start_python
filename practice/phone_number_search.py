'''
n phone numbers,m string, return every string's count in those p_ns
'''


def search_count(phone_number: list, strings: list):
    result_count = []
    for sub_str in strings:
        count = 0
        for number in phone_number:
            if sub_str in number:
                count = count + 1
        result_count.append(count)
    return result_count


print(search_count(['12341243', '1235676798'], ['123', '798']))
