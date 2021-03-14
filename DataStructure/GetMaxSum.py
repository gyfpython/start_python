class MaxSum(object):

    def get_max(self, arr):
        if not arr:
            return False
        if len(arr) == 1:
            return arr[0]
        max_sum, result = arr[0], arr[0]
        for i in arr[1:]:
            if max_sum < 0:
                max_sum = i
            else:
                max_sum += i
            result = max(result, max_sum)
        return result


if __name__ == "__main__":
    test_list = [-4, 18, -2, -3, 5, 6, -11, 8, 9]
    start = MaxSum()
    print(start.get_max(test_list))