if __name__ == "__main__":
    while True:
        a = int(input())
        b = list(map(int, input().split()))
        num_list = sorted(b)
        num = 0
        for i in range(1, len(num_list)):
            if (num_list[i] - num_list[i-1]) % 10 == 0:
                num = num + (num_list[i] - num_list[i-1])//10 - 1
            else:
                num = num + (num_list[i] - num_list[i - 1]) // 10
        if (num + len(num_list)) % 3 == 0:
            print(num)
        else:
            print(num + (3-(num + len(num_list)) % 3))





