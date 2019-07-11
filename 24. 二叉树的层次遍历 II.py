# 给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）
# 例如：
# 给定二叉树 [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回其自底向上的层次遍历为：
# [
#   [15,7],
#   [9,20],
#   [3]
# ]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        queue = [root]
        target = []
        while queue:
            nodes = []
            values = []
            for node in queue:
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
                values += [node.val]
            target = [values] + target
            queue = nodes
        return target
        