def test1(num: str):
    list1 = list(num)
    num1 = 0
    for i in range(len(list1)):
        num1 = num1 + int(list1[i])
    return num1


if __name__ == '__main__':
    while True:
        num_tem = input()
        while int(num_tem) >= 10:
            num_tem = test1(str(num_tem))
        print(num_tem)
