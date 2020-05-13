import sys
if __name__ == "__main__":
    for i in range(5):
        line = list(map(int, input().split(" ")))
        list1 = list(map(int, input().split(" ")))
        list2 = list(map(int, input().split(" ")))
        result_list = sorted(set(list1 + list2))
        print("".join(map(str, result_list)))



