# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.list_a = []
        self.list_b = []

    def push(self, node):
        self.list_a.append(node)
        # write code here

    def pop(self):
        if not self.list_b:
            for i in range(len(self.list_a)-1, -1, -1):
                self.list_b.append(self.list_a[i])
            self.list_a = []
            print(self.list_b.pop())
            # return self.list_b.pop()
        else:
            print(self.list_b.pop())
            # return self.list_b.pop()
        # return xx


if __name__ == "__main__":
    test1 = Solution()
    test1.push(1)
    test1.push(2)
    test1.push(3)
    test1.pop()
    test1.pop()
    test1.push(4)
    test1.push(5)
    test1.pop()
    test1.pop()
    test1.pop()
