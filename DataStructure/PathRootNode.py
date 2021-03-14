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
            if not node.left and not node.right and targrt == 0:
                res.append(path_)
                return
            if node.left:
                get_path(node.left, path_, targrt)
            if node.right:
                get_path(node.right, path_, targrt)
        get_path(root, [], sum)
        return res
        # write code here


if __name__ == "__main__":
    root = TreeNode(1)
    A = TreeNode(2)
    B = TreeNode(3)
    C = TreeNode(10)
    D = TreeNode(9)
    E = TreeNode(4)
    F = TreeNode(-2)
    G = TreeNode(11)
    root.left = A
    root.right = B
    A.right = C
    A.left = E
    B.right = D
    B.left = F
    F.left = G
    test1 = Solution()
    print(test1.pathSum(root, 13))

    # test2 = []
    #
    # test2.append(root.val)
    # print(test2)