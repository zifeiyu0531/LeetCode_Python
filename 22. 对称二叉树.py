# 给定一个二叉树，检查它是否是镜像对称的。
# 例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# 但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
#     1
#    / \
#   2   2
#    \   \
#    3    3
# 说明:
# 如果你可以运用递归和迭代两种方法解决这个问题，会很加分。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isMirror(root, root)
    
    def isMirror(self, root1: TreeNode, root2: TreeNode) -> bool:
        if root1 == None and root2 == None:
            return True
        elif root1 == None or root2 == None:
            return False
        else:
            return root1.val == root2.val and self.isMirror(root1.left, root2.right) and self.isMirror(root1.right, root2.left)