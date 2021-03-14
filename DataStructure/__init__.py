class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#
#
# @param root TreeNode类
# @return int整型二维数组
#
class Solution:
    def __init__(self):
        self.return_list = []
    def levelOrder(self , root ):
        if not root:
            return []
        self.levelSort([root,])
        return self.return_list
        # write code here
    def levelSort(self, list_1):
        tem_list = []
        new_list = []
        for node in list_1:
                tem_list.append(node.val)
                if node.left:
                    new_list.append(node.left)
                if node.right:
                    new_list.append(node.right)
        self.return_list.append(tem_list)
        self.levelSort(new_list)


if __name__ == "__main__":
    A = TreeNode(1)
    # B = TreeNode(2)
    # C = TreeNode(3)
    # A.left = B
    # A.right = C

    print(Solution().levelOrder(A))


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#
#
# @param root TreeNode类
# @param sum int整型
# @return int整型二维数组
#
class Solution:
    def pathSum(self, root, sum):
        if not root:
            return []
        res = []
        def get_path(node, path, targrt):
            path_ = path + [node.val]
            targrt = targrt - node.val
            # if not node.left and not node.right and targrt == 0:
            #     res.append(path_)
            #     return
            if not node.left and not node.right:
                res.append(path_)
                return
            if node.left:
                get_path(node.left, path_, targrt)
            if node.right:
                get_path(node.right, path_, targrt)
        get_path(root, [], sum)
        return res


if __name__ == "__main__":
    root = TreeNode(1)
    A = TreeNode(2)
    B = TreeNode(3)
    C = TreeNode(10)
    D = TreeNode(9)
    E = TreeNode(4)
    root.left = A
    root.right = B
    A.right = C
    A.left = E
    B.right = D
    test1 = Solution()
    print(test1.pathSum(root, 13))

    # test2 = []
    #
    # test2.append(root.val)
    # print(test2)