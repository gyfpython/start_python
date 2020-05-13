if __name__ == "__main__":
    while True:
        line = list(map(int, input().split()))
        price = line[0]
        num = line[1]
        price_list = sorted(list(map(int, input().split())))
        test = []
        for i in range(num):
            test.append(input())
        set_test = set(test)
        number = []
        for app in set_test:
            number.append(test.count(app))
        result_number = sorted(number, reverse=True)
        min_price, max_price = 0, 0
        for i in range(len(result_number)):
            min_price = min_price + result_number[i]*price_list[i]
            max_price = max_price + result_number[i]*price_list[-(i+1)]
        print(min_price, max_price)




