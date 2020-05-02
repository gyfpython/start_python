
def get_binary_tree(numbers: list):
    result_list = numbers
    print(numbers)
    while len(numbers) > 1:
        numbers, test_num = get_next_number(numbers)
        result_list = result_list + numbers
        # print(numbers)
        if test_num:
            numbers.insert(0, test_num)
        print(numbers)
    return result_list


def get_next_number(numbers: list):
    tem_list = []
    temp_num = None
    if len(numbers) % 2 == 0:
        for i in range(len(numbers)//2):
            tem_list.append(numbers[2*i] + numbers[2*i+1])
    else:
        for i in range(len(numbers)//2):
            tem_list.append(numbers[2*i+1] + numbers[2*i+2])
            temp_num = numbers[0]
    return tem_list, temp_num


print(get_binary_tree([15, 7, 6, 6, 5, 4, 3, 3, 3]))
