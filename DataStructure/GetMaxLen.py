#
#
# @param arr int整型一维数组 the array
# @return int整型
#
class Solution:
    def maxLength(self, arr):
        for i in range(len(arr)-1, -1, -1):
            for j in range(len(arr) - i):
                tem_arr = arr[j: j+i+1]
                if len(list(set(tem_arr))) == 1 + i:
                    return i + 1
        # write code here


if __name__ == "__main__":
    test1 = Solution()
    print(test1.maxLength([1, 2, 3]))
