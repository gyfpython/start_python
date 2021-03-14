#
# 二分查找
# @param n int整型 数组长度
# @param v int整型 查找值
# @param a int整型一维数组 有序数组
# @return int整型
#
class Solution:
    def upper_bound_(self, n, v, a):
        # write code here
        start_find = 0
        end_find = n
        while True:
            if start_find != end_find and end_find - start_find > 1:
                if a[(start_find + end_find) // 2] >= v:
                    end_find = (start_find + end_find) // 2
                else:
                    start_find = (start_find + end_find) // 2
            elif start_find == end_find:
                return start_find + 1
            else:
                if a[start_find] >= v:
                    return start_find + 1
                else:
                    return end_find + 1


if __name__ == "__main__":
    test1 = Solution()
    print(test1.upper_bound_(5, 3, [1, 2, 4, 4, 5]))
