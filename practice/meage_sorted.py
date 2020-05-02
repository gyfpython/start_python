'''
meage two list and sorted
'''


def test(list1: list, list2: list):
    for ele in list2:
        list1.append(ele)
    n = len(list1)
    for k in range(n-1):
        for i in range(n-k-1):
            if list1[i] > list1[i+1]:
                list1[i], list1[i+1] = list1[i+1], list1[i]

    return list1


test_list1 = ['1', 'c']
test_list2 = ['b', '0']
print(test(test_list1, test_list2))
